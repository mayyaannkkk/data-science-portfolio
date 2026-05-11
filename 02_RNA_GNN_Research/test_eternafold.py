import dotenv
dotenv.load_dotenv('.env')
from src.data.sec_struct_utils import predict_sec_struct
result = predict_sec_struct('GGGAAACCC')
print('EternaFold result:', result)