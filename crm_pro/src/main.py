from database import create_table
from dashboard import Dashboard

create_table()

app = Dashboard()

app.mainloop()