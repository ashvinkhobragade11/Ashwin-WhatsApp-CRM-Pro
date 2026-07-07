from database import create_table, create_users_table
from modules.auth.user_manager import create_default_admin
from modules.auth.login import LoginWindow

create_table()
create_users_table()
create_default_admin()

app = LoginWindow()

app.mainloop()