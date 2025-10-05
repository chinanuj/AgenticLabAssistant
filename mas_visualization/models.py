# models.py
import sqlalchemy
from mas_visualization.database import metadata

#'users' table
users = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("username", sqlalchemy.String, unique=True, index=True),
    sqlalchemy.Column("full_name", sqlalchemy.String),
    sqlalchemy.Column("email", sqlalchemy.String, unique=True, index=True),
    sqlalchemy.Column("hashed_password", sqlalchemy.String),
    sqlalchemy.Column("role", sqlalchemy.String, default="student"),
)

#'labs' table
labs = sqlalchemy.Table(
    "labs",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String, unique=True),
    sqlalchemy.Column("capacity", sqlalchemy.Integer),
    sqlalchemy.Column("description", sqlalchemy.Text, nullable=True),
    sqlalchemy.Column("equipment", sqlalchemy.String, nullable=True),
    sqlalchemy.Column("operating_start_time", sqlalchemy.Time, nullable=True),
    sqlalchemy.Column("operating_end_time", sqlalchemy.Time, nullable=True),
)

bookings = sqlalchemy.Table(
    "bookings",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("lab_id", sqlalchemy.Integer, sqlalchemy.ForeignKey("labs.id")),
    sqlalchemy.Column("user_id", sqlalchemy.Integer, sqlalchemy.ForeignKey("users.id")),
    
    # FIX: Add (timezone=True) to both DateTime columns
    sqlalchemy.Column("start_time", sqlalchemy.DateTime(timezone=True)),
    sqlalchemy.Column("end_time", sqlalchemy.DateTime(timezone=True)),

    sqlalchemy.Column("student_count", sqlalchemy.Integer),
    sqlalchemy.Column("booked_by", sqlalchemy.String),
    sqlalchemy.Column("priority", sqlalchemy.Integer, default=3),
)
