from boto.mturk.connection import MTurkConnection
from boto.mturk.question import ExternalQuestion


######  CONFIGURATION PARAMETRS  ######

SANDBOX = True  # Select whether to post to the sandbox (using fake money), or live MTurk site (using REAL money)
HIT_URL = "Congren.github.io"  # Provide the URL that you want workers to sent sent to complete you task

NUMBER_OF_HITS = 1  # Number of different HITs posted for this task
NUMBER_OF_ASSIGNMENTS = 1  # Number of tasks that DIFFERENT workers will be able to take for each HIT
LIFETIME = 60 * 60 * 24  # How long that the task will stay visible if not taken by a worker (in seconds)
REWARD = 0.04  # Base payment value for completing the task (in dollars)
DURATION = 60*5  # How long the worker will be able to work on a single task (in seconds)
APPROVAL_DELAY = 60*60*2  # How long after the task is completed will the worker be automatically paid if not manually approved (in seconds)


# HIT title (as it will appear on the public listing)
TITLE = 'Falling Block Game'
# Description of the HIT that workers will see when deciding to accept it or not
DESCRIPTION = 'Fill in a more detailed explaination of the task that needs to be performed (1-3 sentences should be enough).'
# Search terms for the HIT posting
KEYWORDS = ['Game', 'Falling', 'Fun']


# Your Amazon Web Services Access Key (private)
AWS_ACCESS_KEY = 'AKIAI5XH6NUQH52GJXOQ' # <-- TODO: Enter your access key here
# Your Amazon Web Services Secret Key (private)
AWS_SECRET_KEY = 'Vx+/U246KUqkpk0uWtMWXG4R4477RPiF+ltlD4Ed' # <-- TODO: Enter your private key here

#######################################


def create_hits():
	if SANDBOX:
		mturk_url = 'mechanicalturk.sandbox.amazonaws.com'
		preview_url = 'https://workersandbox.mturk.com/mturk/preview?groupId='
	else:
		mturk_url = 'mechanicalturk.amazonaws.com'
		preview_url = 'https://mturk.com/mturk/preview?groupId='

	q = ExternalQuestion(external_url=HIT_URL, frame_height=800)
	conn = MTurkConnection(aws_access_key_id=AWS_ACCESS_KEY, aws_secret_access_key=AWS_SECRET_KEY, host=mturk_url)
	for i in range(0, NUMBER_OF_HITS):
		create_hit_rs = conn.create_hit(question=q, lifetime=LIFETIME, max_assignments=NUMBER_OF_ASSIGNMENTS, title=TITLE, keywords=KEYWORDS, reward=REWARD, duration=DURATION, approval_delay=APPROVAL_DELAY, annotation=DESCRIPTION)
		print(preview_url + create_hit_rs[0].HITTypeId)
		print("HIT ID: " + create_hit_rs[0].HITId)
    
if __name__ == "__main__":
	create_hits()

