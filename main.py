from typing import List, Any
from datetime import datetime


class Developer:
 
	"""
	A class used to represent a developer
	
	...
    Attributes
    ----------
    _id : int
        id of the developer
    full_name : str
        name and surname of the developer
    address : str
        relevant address
    email : str
        e-mail for work
    phone_number : str
        phone number for work
    position : str
        current position at the company
    salary : float
        income
    projects : list[Projects]
        list of projects developer working on now
    assignments : list[Assignment]:
        list of assignments
    """
    
	def __init__(self, id: int, name: str, address: str, phone_number: str,email: str, position: int, rank: int,salary: float) -> None:
		"""
		Method to add a developer
	    ----------
	    _id : int
	        id of the developer
	    full_name : str
	        name and surname of the developer
	    address : str
	        relevant address
	    email : str
	        e-mail for work
	    phone_number : str
	        phone number for work
	    position : str
	        current position at the company
	    salary : str
	        income
	    projects : list[Projects]
	        list of projects developer working on now
	    assignments : list[Assignment]:
	        list of assignments
	    """
		self.id = id
		self.name = name
		self.address = address
		self.phone_number = phone_number
		self.email = email
		self.position = position
		self.rank = rank
		self.salary = salary
		self.assignments = []
		self.projects: List[Any] = []
		
	#*def assign_possibility(self):"
	#if newProject.limit>=newProject.developers.len:
	#   return True
	#else
	#   :return False
	

	def assigned_projects(self) -> List[Any]:
		"""
		Method to get the list of developer`s current projects.
		-------------
		No parameters
		-------------
		Returns : list[Project]
		"""
		return self.projects
	 
	def assign(self, project) -> None:
		"""
		Method to add developer to new project.
		----------
		Parameters
		----------
		project : Project
			Enter the project you want assign developer to
		-------------
		Returns : None
		"""
		self.projects.append(project)


class Assignment:
	"""
	A class used to represent an assignment
	...
    Attributes
    ----------
    received_tasks : dict
        task to do
    is_done : bool
        Is task done or not
    description : str
        short information about the task
    status : str
        current status of the assignment
    """
	def __init__(self, received_tasks: dict, is_done: bool, description: str, status: str) -> None:
		"""
		Method to create an assignment
		...
	    Attributes
	    ----------
	    received_tasks : dict
	        task to do
	    is_done : bool
	        rather
	    description : str
	        short information about the task
	    status : str
	        current status of the assignment
	    """
		self.received_tasks = received_tasks
		self.is_done = is_done
		self.description = description
		self.status = status
	def get_tasks_to_date(self, date: datetime):
		"""
		Returns task before date from parameters.
		-----------
		Parameters
		Date : datetime
		-------------
		Returns : list[Project]
		"""
		return [i for i2, i in self.received_tasks.items() if i2 <= date]


class Project:
	
	"""
	A class used to represent a project
	
	...
    Attributes
    ----------
    title : str
        name of the project
    start_date : datetime
        date when project have to start
    task_list : list[dict]
        list of tasks need to be completed
    developers : list[Developer]
        list of the developer working on this project
    limit : int
        limit of the developers can be working on this project at once
    """
	
	def __init__(self, title: str, start_date: datetime, task_list: list[dict],developers: list[Developer], limit: int) -> None:
		"""
		A method used to create a project
		
		...
	    Attributes
	    ----------
	    title : str
	        name of the project
	    start_date : datetime
	        date when project have to start
	    task_list : list[dict]
	        list of tasks need to be completed
	    developers : list[Developer]
	        list of the developer working on this project
	    limit : int
	        limit of the developers can be working on this project at once
	    """
		self.title = title
		self.start_date = start_date
		self.task_list = task_list
		self.developers = developers
		self.limit = limit
		
	def add_developer(self, developer: Developer) -> None:
		"""
		Method used to add a developer to project
		-----------
		Parameters
		developer : Developer
		-------------
		Returns : None
		"""
		if self.limit > len(self.developers):
			self.developers.append(developer)
			developer.assign(project=self)

	def remove_developer(self, developer: Developer) -> None:
		"""
		Method used to add a developer to project
		-----------
		Parameters
		developer : Developer
		-------------
		Returns : None
		"""
		for i in self.developers:
			if i.id == developer.id:
				self.developers.remove(self.developers.index(i))
				return
		return

class QAEngineer:
	
	"""
	A class used to represent a QAEngineer
	
	...
    Attributes
    ----------
    id : int
        id of QAEngineer
    name : str
        name of the QAEngineer
    address : str
        relevant address of the QAEngineer
    phone_number : str
        phone number of the QAEngineer (work only)
    email : str
        email of the QAEngineer (work only)
    salary : float
        income
    rank : str
        current position in the company
    position : str
        current position in the company
    """
	
	def __init__(self, id: int, name: str, address: str, phone_number: str,email: str, salary: float, rank: str, position: str) -> None:
		"""
		A method used to add a QAEngineer
		
		...
	    Attributes
	    ----------
	    id : int
	        id of QAEngineer
	    name : str
	        name of the QAEngineer
	    address : str
	        relevant address of the QAEngineer
	    phone_number : str
	        phone number of the QAEngineer (work only)
	    email : str
	        email of the QAEngineer (work only)
	    salary : float
	        income
	    rank : str
	        current position in the company
	    position : str
	        current position in the company
	    """
		self.id = id
		self.name = name
		self.address = address
		self.phone_number = phone_number
		self.email = email
		self.salary = salary
		self.rank = rank
		self.position = position

	def test_feature(self , *args) -> None:
		"""
		Method used to test a feature
		-----------
		Parameters
		*args : any
			depends on feature you are testing
		-------------
		Returns : None
		"""
		return


class ProjectManager:
	
	"""
	A class used to represent a QAEngineer
	
	...
    Attributes
    ----------
    id : int
        id of ProjectManager
    name : str
        name of the ProjectManager
    address : str
        relevant address of the ProjectManager
    phone_number : str
        phone number of the ProjectManager (work only)
    email : str
        email of the ProjectManager (work only)
    salary : float
        income
    project : Project
        current project , ProjectManager working on
    """
 
	def __init__(self, id: int, name: str, address: str, phone_number: str,email: str, salary: float, project: Project) -> None:
		"""
		A method used to add a QAEngineer
		
		...
	    Attributes
	    ----------
	    id : int
	        id of ProjectManager
	    name : str
	        name of the ProjectManager
	    address : str
	        relevant address of the ProjectManager
	    phone_number : str
	        phone number of the ProjectManager (work only)
	    email : str
	        email of the ProjectManager (work only)
	    salary : float
	        income
	    project : Project
	        current project , ProjectManager working on
	    """
		self.id = id
		self.name = name
		self.address = address
		self.phone_number = phone_number
		self.email = email
		self.salary = salary
		self.project = project

	def discuss_progress(developer: Developer):
		"""
		Method used to discuss progress of the current task
		with one of the developers in the project
		-----------
		Parameters
		developer : Developer
			The developer you want to have discussion with
		-------------
		Returns : None
		"""
		return


print(help(Developer))