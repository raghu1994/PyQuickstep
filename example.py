import pyquickstep

conn = pyquickstep.Connect('localhost', '3000')
cursor = conn.cursor()
print cursor.execute("select * from weather")