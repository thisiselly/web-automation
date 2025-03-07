import os
class GetFilePage:
    # this is project path
    project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    #get log path
    get_log_path = os.path.join(project_path, "logs")

    #get csv path
    get_csv_path = os.path.join(project_path, r"data\testdata.csv")

# if __name__ == '__main__':
#     print(GetFilePage.get_log_path)
#     print(GetFilePage.get_csv_path)
