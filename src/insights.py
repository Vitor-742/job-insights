from src.jobs import read


def get_unique_job_types(path):
    listData = []

    data = read(path)
    for item in data:
        listData.append(item["job_type"])

    return set(listData)


def filter_by_job_type(jobs, job_type):
    dataList = []
    for job in jobs:
        if job['job_type'] == job_type:
            dataList.append(job)
    return dataList


def get_unique_industries(path):
    listData = []

    data = read(path)
    for item in data:
        listData.append(item["industry"])

    # del listData['']
    # filterData = set(listData)
    # if(filterData.count('') > 0):
    #     filterData.remove('')
    filterData = [x for x in listData if x != '']
    # if('' in listData):
    #     print('a')
    #     listData.remove('')
    return set(filterData)


def filter_by_industry(jobs, industry):
    dataList = []
    for job in jobs:
        if job['industry'] == industry:
            dataList.append(job)
    return dataList


def get_max_salary(path):
    max = 0
    data = read(path)
    for item in data:
        if item['max_salary'].isdigit():
            if int(item['max_salary']) > max:
                max = int(item['max_salary'])
    return max


def get_min_salary(path):
    first = True
    data = read(path)
    for item in data:
        if item['min_salary'].isdigit():
            if first:
                min = int(item['min_salary'])
                first = False
            if int(item['min_salary']) < min:
                min = int(item['min_salary'])
    return min


def matches_salary_range(job, salary):
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    pass


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    return []
