"""
Simple smoke script to exercise UserDatabase API and confirm runtime behavior.
"""
from src.user_database import UserDatabase

print('Starting smoke test for UserDatabase...')

db = UserDatabase()

db.add_user(1000, {'name': 'John Doe'})
db.add_user(500, {'name': 'Jane Smith'})
db.add_user(750, {'name': 'Bob Johnson'})

print('All user IDs (inorder):', db.get_all_user_ids())
print('Is index balanced?:', db.is_index_balanced())
print('Get user 750:', db.get_user(750))

print('Smoke test completed successfully.')
