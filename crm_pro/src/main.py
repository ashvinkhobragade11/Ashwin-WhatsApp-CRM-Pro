from database import create_table
from dashboard import Dashboard
from modules.auth.user_manager import create_default_admin

create_table()
create_default_admin()

app = Dashboard()

app.mainloop()