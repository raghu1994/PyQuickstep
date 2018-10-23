import pyquickstep

conn = pyquickstep.Connect('localhost', '3000')
cursor = conn.cursor()
result = cursor.execute("select * from weather")
print cursor._rows
print result