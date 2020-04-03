import numpy as np

def get_clickthrough_rates(packages, package_ids):
    package_ids_with_clickthrough = []
    for package_id in package_ids:
        impressions = packages[package_id]['impressions']
        clicks = packages[package_id]['clicks']
        package_ids_with_clickthrough.append((package_id, int(clicks)/int(impressions)))
        
    return((package_ids_with_clickthrough))

def create_pairwise_matrix(packages_with_clickthrough_with_treatment, 
                           packages_with_clickthrough_without_treatment, 
                           properties_to_contrast, is_valid_comparison):
    
    rows = len(packages_with_clickthrough_with_treatment)
    cols = len(packages_with_clickthrough_without_treatment)
    
    # if there is not at least one package with an treatment and one package 
    # without the treatment, then this test is not valid
    if rows == 0 or cols == 0:
        return None
    
    # initialize a matrix, setting everything to NaN (None)
    pairwise_clickthrough_rates_difference_matrix = np.empty([rows, cols])
    pairwise_clickthrough_rates_difference_matrix[:] = np.NaN
    
    for i,with_treatment_package in enumerate(packages_with_clickthrough_with_treatment):
        with_treatment_package_id = with_treatment_package[0]
        with_treatment_clickthrough_rate = with_treatment_package[1]
        
        for j, no_treatment_package in enumerate(packages_with_clickthrough_without_treatment):
            no_treatment_package_id = no_treatment_package[0]
            no_treatment_clickthrough_rate = no_treatment_package[1]
            
            # check that the headline is the only thing that's different
            packages_are_comparable = is_valid_comparison(with_treatment_package_id, 
                                                          no_treatment_package_id, 
                                                          properties_to_contrast)
            
            #if nothing else is difference
            if packages_are_comparable:
                # calculate the difference between each celeb and no celeb package
                pairwise_clickthrough_rates_difference_matrix[i][j] = \
                    with_treatment_clickthrough_rate - no_treatment_clickthrough_rate
    
    return pairwise_clickthrough_rates_difference_matrix

def insert_to_valid_tests(desired_treatment_size, valid_tests, test_id, \
                          has_treatment_package_id, no_treatment_package_id):
    if test_id not in valid_tests.keys():
        valid_tests[test_id] = {}
    valid_tests[test_id][desired_treatment_size] = {}
    valid_tests[test_id][desired_treatment_size]['treatment'] = has_treatment_package_id
    valid_tests[test_id][desired_treatment_size]['no_treatment'] = no_treatment_package_id
    return valid_tests
    
#desired_treatment_size = "min" or "max"
def get_comparisons(desired_treatment_size, pairwise_clickthrough_rates_difference_matrix, 
                    packages_with_clickthrough_with_treatment, 
                    packages_with_clickthrough_without_treatment):
    # if we want the minimum effect size, we take where the difference is in favour
    # of no treatment
    if desired_treatment_size == "min":
        matrix_index = np.where(pairwise_clickthrough_rates_difference_matrix == \
                       np.nanmin(pairwise_clickthrough_rates_difference_matrix))
    else:
        matrix_index = np.where(pairwise_clickthrough_rates_difference_matrix == \
                        np.nanmax(pairwise_clickthrough_rates_difference_matrix))
        
    with_treatment_matrix_idx = matrix_index[0][0]
    no_treatment_matrix_idx = matrix_index[1][0]
    with_treatment_package_id = packages_with_clickthrough_with_treatment[with_treatment_matrix_idx][0]
    no_treatment_package_id = packages_with_clickthrough_without_treatment[no_treatment_matrix_idx][0]
    
    return with_treatment_package_id, no_treatment_package_id

# function takes in the treatment you are trying to test for
# e.g. whether or not a property has a number
# it also takes in which properties you want to contrast
# for example, a headline or a lede

def get_valid_tests(tests, packages, has_treatment, is_valid_comparison, properties_to_contrast):

    # iterate through every test, create a matrix
    i = 0
    total_valid_tests = 0
    valid_tests = {}
    for t,test in tests.items():
        package_ids = test['package_ids']

        # packages that match criteria vs packages that don't match criteria
        packages_with_treatment = []
        packages_without_treatment = []

        for package_id in package_ids:
            
            package_meets_condition = 0
            for col in properties_to_contrast:
                value = packages[package_id][col]
                if has_treatment(value):
                    package_meets_condition = 1
            
            packages_with_treatment.append(package_id) if package_meets_condition == 1 \
                else packages_without_treatment.append(package_id)

        # for each package, get what the clickthrough rates are
        packages_with_clickthrough_with_treatment = get_clickthrough_rates(packages, packages_with_treatment)
        packages_with_clickthrough_without_treatment = get_clickthrough_rates(packages, packages_without_treatment)

        # create a matrix
        pairwise_clickthrough_rates_difference_matrix = \
            create_pairwise_matrix(packages_with_clickthrough_with_treatment, 
                                        packages_with_clickthrough_without_treatment,
                                   properties_to_contrast, is_valid_comparison
                                  )

        if pairwise_clickthrough_rates_difference_matrix is None or \
            np.isnan(pairwise_clickthrough_rates_difference_matrix).all():
            pass
        else:
            total_valid_tests+=1

            # min is the worst performing celeb headline and 
            # best performing non-celeb headline
            
            min_treatment_package_id, max_no_treatment_package_id = \
                get_comparisons("min", pairwise_clickthrough_rates_difference_matrix,
                               packages_with_clickthrough_with_treatment,
                               packages_with_clickthrough_without_treatment)

            max_treatment_package_id, min_no_treatment_package_id = \
                get_comparisons("max", pairwise_clickthrough_rates_difference_matrix,
                               packages_with_clickthrough_with_treatment,
                               packages_with_clickthrough_without_treatment)

            valid_tests = insert_to_valid_tests("min", valid_tests, t, \
                                                min_treatment_package_id, max_no_treatment_package_id)
            valid_tests = insert_to_valid_tests("max", valid_tests, t, \
                                                max_treatment_package_id, min_no_treatment_package_id)        

    print("There are {0} valid tests that match the given criteria.".format(total_valid_tests))
    return valid_tests

def get_properties(packages, package_id):
    clicks = int(packages[package_id]['clicks'])
    impressions = int(packages[package_id]['impressions'])
    headline_idx = packages[package_id]['headline_idx']
    return clicks, impressions, headline_idx
