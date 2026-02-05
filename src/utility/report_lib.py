import datetime
import os

#ensure the report directory exists
project_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))+"/report"
#report_file  = os.path.join(project_path,'report')
os.makedirs(project_path, exist_ok=True)

timestamp = datetime.datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
report_filename = os.path.join(project_path,f"report_{timestamp}.txt")


def write_output(validation_type,status,details,table):
    with open(report_filename,"a") as f:
        f.write(f"Type of validation : {validation_type} \n Status : {status} \n Details : {details}\n table: {table}\n\n")



