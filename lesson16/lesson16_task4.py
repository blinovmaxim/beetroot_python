class CustomException(Exception):
    def __init__(self,msg):
        super().__init__(msg)

msg="Exception Triggered! Something went wrong."
with open("logs.txt", "w") as f:
    f.write(msg)
raise CustomException(msg)
        