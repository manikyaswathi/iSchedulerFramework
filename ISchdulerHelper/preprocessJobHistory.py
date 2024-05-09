import pandas as pd
from datetime import datetime, timedelta
import csv

import sys
# import job  # This should be a module that contains the definition of the Job information

new_column_labels = ['jobid', 'user', 'account', 'start', 'end', 'submit', 
                     'queue', 'max_minutes', 'jobname', 'state', 'nnodes', 
                     'reqcpus', 'nodelist', 'qos']


def label_and_save_csv(input_file_path, output_file_path, column_labels):
    try:
        df = pd.read_csv(input_file_path, header=None)

        df.columns = column_labels

        df.to_csv(output_file_path, index=False)
        print(f'File saved successfully to {output_file_path}')
    except Exception as e:
        print(f'An error occurred: {e}')

# def parse_job_TACC(log, job_filter=None):
#     job_dict = {}
#     with open(log) as f:
#         reader = csv.reader(f, delimiter=',')
#         next(reader, None) 
#         for row in reader:
#             # if row[0].strip() in ['90810', '108114', '103943', '102933']:
#             #     continue
#             start_time = datetime.strptime(row[3].strip(), "%Y-%m-%d %H:%M:%S")
#             end_time = datetime.strptime(row[4].strip(), "%Y-%m-%d %H:%M:%S")
#             submit_time = datetime.strptime(row[5].strip(), "%Y-%m-%d %H:%M:%S")
#             queueName = row[6].strip()
#             if job_filter is not None:
#                 if any(filter_item[0] <= submit_time < filter_item[1] for filter_item in job_filter):
#                     continue
#             if (end_time - start_time).total_seconds() > (int(row[7]) * 60):
#                 end_time = start_time + timedelta(seconds=int(row[7]) * 60)
#             new_job = job.Job(row[0], int(row[10]), start_time, submit_time, end_time, int(row[7]))
#             # if pivot is not None and new_job.duration.total_seconds() / (new_job.time_limit * 60) < pivot:
#             #     continue
#             job_dict[row[0]] = {'job': new_job, 'queueName': queueName}
#     return job_dict



label_and_save_csv(sys.argv[1], sys.argv[2], new_column_labels)

