import pyquickstep

conn = pyquickstep.Connect('localhost', '3000')
cursor = conn.cursor()
result = cursor.execute("select * from weather")


print cursor.fetchone()
print cursor.fetchmany()
print cursor.fetchall()