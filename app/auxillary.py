import datetime,pytz

def allowed_file(filename):
    return filename.endswith(('.png','.jpg'))

def get_date():
    """Return datetime object with current date"""
    jamaica = pytz.timezone("America/Jamaica")
    return datetime.datetime.now(jamaica)

def get_file_extension(filename):
    """Returns file extension for a given filename"""
    return filename.split(".")[-1]

def format_date(datetimeObject):
    """Formats a datetime object as 
        Day Month, Year"""
    return datetimeObject.strftime("%B %d, %Y")
    
    
