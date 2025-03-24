import sqlite3

# Ma'lumotlar bazasiga ulanish
conn = sqlite3.connect("bot_database.db")
cursor = conn.cursor()

# Foydalanuvchilar jadvalini yaratish
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY,
    inviter_id INTEGER,
    points INTEGER DEFAULT 0
)
""")
conn.commit()

# Yangi foydalanuvchini qo‘shish
def add_user(user_id, inviter_id=None):
    cursor.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))
    user = cursor.fetchone()
    if not user:
        cursor.execute("INSERT INTO users (user_id, inviter_id, points) VALUES (?, ?, ?)", (user_id, inviter_id, 0))
        if inviter_id:
            cursor.execute("UPDATE users SET points = points + 1 WHERE user_id = ?", (inviter_id,))
        conn.commit()

# Ochkolarni olish
def get_points(user_id):
    cursor.execute("SELECT points FROM users WHERE user_id = ?", (user_id,))
    result = cursor.fetchone()
    return result[0] if result else 0
