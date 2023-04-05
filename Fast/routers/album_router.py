from fastapi import FastAPI,APIRouter,Depends,HTTPException
from fastapi.security import HTTPBasic,HTTPBasicCredentials
from util import album_util
import Constants
import fetch_data
import jwt
from datetime import datetime, timedelta

app = FastAPI()
security = HTTPBasic()

router=APIRouter(prefix='/album')

# Secret key used for encoding and decoding tokens
SECRET_KEY = "mysecretkey"

# Function to generate a token for a user
def generate_token(user_data: dict):

    to_encode = user_data.copy()
    expire = datetime.utcnow() + timedelta(minutes=1)
    to_encode.update({"exp": expire})

    token = jwt.encode(to_encode, SECRET_KEY)
    return token

# Function to decode a token and verify its signature
def decode_token(token: str):

    try:
        decoded_token = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return True
    except jwt.exceptions.ExpiredSignatureError:
        return "Token is invalid as Expired"
    except jwt.exceptions.InvalidSignatureError:
        return "Wrong Token Entered"    
    except jwt.exceptions.DecodeError:
        return "Wrong Token Entered"
    
@router.get("/token/")
async def get_token(credentials: HTTPBasicCredentials = Depends(security)):
    username = credentials.username
    password = credentials.password
    USER_DATA = {
        "username": username,
        "email":password,
        "is_active": True
    }
    global user_name
    global pass_word
    user_name=username
    pass_word=password

    token = generate_token(USER_DATA)
    return {"token": token}

@router.get("/album-data")
def album( token: str, decoded_token: dict = Depends(decode_token)):

    if decoded_token!="Token is invalid as Expired" and decoded_token!="Wrong Token Entered" :
        user = fetch_data.get_db_data(Constants.user_auth_query.format(username = user_name, password=pass_word))   
        if user:
            return album_util.album_data()    
        else:
            raise HTTPException(status_code=403)   
             
    elif decoded_token=="Token is invalid as Expired":
        return {"message": "Token is invalid as Expired"}
    elif decoded_token=="Wrong Token Entered":
         return {"message": "Wrong Token Entered"}
    else:
        return {"message": "Error"}

    
    