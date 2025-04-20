from sqlalchemy import create_engine, inspect

# Create engine passing connection string
tt_bd = create_engine('postgresql://postgres:ttPas05%40@localhost:5432/ticket_tracker')

# Create an inspector
inspector = inspect(tt_bd)

# Print tables' names
print(inspector.get_table_names())