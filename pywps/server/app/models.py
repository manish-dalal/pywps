from main import db

class Request(db.Model):
	uuid = db.Column(db.String(length=255), nullable=False, primary_key=True)
	pid = db.Column(db.Integer)
	operation = db.Column(db.String(length=30), nullable=False)
	version = db.Column(db.String(length=5), nullable=False)
	time_start = db.Column(db.Text, nullable=False)
	time_end = db.Column(db.Text)
	identifier = db.Column(db.Text)
	message = db.Column(db.Text)
	percent_done = db.Column(db.Float)
	status = db.Column(db.String(length=30))

	def __init__(uuid, pid, operation, version, time_start, time_end, identifier, message, percent_done, status):
		self.uuid = uuid
		self.pid = pid
		self.operation = operation
		self.version = version
		self.time_start  = time_start
		self.time_end = time_end
		self.identifier = identifier
		self.message = message
		self.percent_done = percent_done
		self.status = status

class StoredRequest(db.Model):
	uuid = db.Column(db.String(length=255), nullable=False, primary_key=True)
	request = db.Column(db.LargeBinary)

	def __init__(uuid, request):
		self.uuid = uuid
		self.request = request
