from db import db

class RequestModel(db.Model):

	__tablename__ = 'requests'

	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(80))
	status = db.Column(db.String(80))
	price = db.Column(db.Float(precision=2))

	def __init__(self, req_id, title, status, price):
		self._id = req_id
		self.title = title
		self.status = status
		self.price = price

	def json(self):
		return {'id': self.id, 'title': self.title, 'status': self.status, 'price': self.price}

	@classmethod
	def find_by_title(cls, title):
		return cls.query.filter_by(title=title).first()

	@classmethod
	def find_by_id(cls, req_id):
		return cls.query.filter_by(id=req_id).first()

	def save_to_db(self):
		db.session.add(self)
		db.session.commit()

	def delete_from_db(self):
		db.session.delete(self)
		db.session.commit()
		
	"""def find_by_title(cls, title):
					connection = sqlite3.connect('data.db')
					cursor = connection.cursor()
			
					query = "SELECT * FROM requests WHERE title=?"
					result = cursor.execute(query, (title,))
					row = result.fetchone()
					if row:
						request = cls(*row)
					else:
						request = None
			
					connection.close()
					return request
			
				def find_by_id(cls, req_id):
					connection = sqlite3.connect('data.db')
					cursor = connection.cursor()
			
					query = "SELECT * FROM requests WHERE id=?"
					result = cursor.execute(query, (req_id,))
					row = result.fetchone()
					if row:
						request = cls(*row)
					else:
						request = None
			
					connection.close()
					return request
			
				def insert(self):
					connection = sqlite3.connect('data.db')
					cursor = connection.cursor()
			
					query = "INSERT INTO requests VALUES (?, ?, ?, ?)"
					cursor.execute(query, (self.title, self.status, self.price))
					row = result.fetchone()
			
					connection.commit()
					connection.close()
			
				def update(self):
					connection = sqlite3.connect('data.db')
					cursor = connection.cursor()
			
					query = "UPDATE requests SET price=? WHERE title=?"
					cursor.execute(query, (self.title, self.price))
					row = result.fetchone()
					
					connection.commit()
					connection.close()"""