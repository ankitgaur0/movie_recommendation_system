import os,sys

class Custom_Exception(Exception):
    def __init__(self,error,error_details:sys):
        self.erorr_message=error
        _,_,tb_exc=error_details.exc_info()

        self.line_num=tb_exc.tb_lineno
        self.file_name=tb_exc.tb_frame.f_code.co_filename

    def __str__(self) -> str:
        return f"the file name is :{self.line_num} \n the line number :{self.line_num} \n error : {str(self.erorr_message)}"