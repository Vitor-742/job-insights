from functools import lru_cache
import csv


@lru_cache
def read(path):
    """Reads a file from a given path and returns its contents

    Parameters
    ----------
    path : str
        Full path to file

    Returns
    -------
    list
        List of rows as dicts
    """

    listData = []

    with open(path, encoding="utf-8") as jobs_file:
        CSVreader = csv.reader(jobs_file, delimiter=",", quotechar='"')
        header, *data = CSVreader
        print(header)

    for item in data:
        job = {}
        for i in range(13):
            job.update({header[i]: item[i]})
        listData.append(job)

    return listData
