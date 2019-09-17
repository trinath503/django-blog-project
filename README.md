<p align="center"><img src="https://neuralmarker-logos.s3-us-west-2.amazonaws.com/logo.png"></p>

<p align="center">
  <a href="#features">Features</a> •
  <a href="https://github.com/jsbroks/coco-annotator/wiki">Wiki</a> •
  <a href="https://github.com/jsbroks/coco-annotator/wiki/Getting-Started">Getting Started</a> •
  <a href="https://github.com/jsbroks/coco-annotator/issues">Issues</a> •
</p>


# Get Started
- Install docker & docker composer, [Installation Guide](https://docs.google.com/document/d/1DAoNNX8xjUm53rHAAz2VrVI5b77teguNBx4uccrPQ9A/edit?usp=sharing)
- For Devlopment --- docker-compose -f docker-compose.dev.yml up --build 
  For Production --- docker-compose -f docker-compose.build.yml up --build 
  <ul>
  <li>First time it will take time to pull images used in dockerfile and install all node & python packages</li>
  <li>Basically docker-compose will create new container (use same if already exist with the same name) sepearated one for frontend (webclient), second for backend server(webserver), third for webworker(for running message queue tasks) and finally database(monngo) [Note: In futher release we will remove it, since migrated to online db storeage(atlas mongo) ] </li>
  <li>To terminate it crtl+c &  docker-compose down (mandatory)</li>
  <li></li>
  </ul>
- (optional) cd scripts/ & pip install -r requirements.txt 


# Tech Stack
### Frontend

- [Vue](https://vuejs.org/) - JavaScript framework for building user interfaces
- [Axios](https://github.com/axios/axios) - Promise based HTTP client
- [PaperJS](http://paperjs.org/) - HTML canvas vector graphics library
- [Bootstrap](https://getbootstrap.com/) - Frontend component library

### Backend

- [Flask](http://flask.pocoo.org/) - Python web microframework
- [MongoDB](https://www.mongodb.com/) - Cross-platform document-oriented database
- [MongoEngine](http://mongoengine.org/) - Python object data mapper for MongoDB
- [Celery](http://www.celeryproject.org/) - Distributed message passing
- [RabbitMQ](http://mongoengine.org/) - Advanced Message Queuing Protocol 

### Others

- AWS S3 - For distriuted image storage
- AWS SES - Sending emails for registratio verification & others
- [Atlas mongo[(https://cloud.mongodb.com) - For cloud database storage
- [Celery](http://www.celeryproject.org/) - Distributed message passing
- [DescriptionRabbitMQ](http://mongoengine.org/) - Advanced Message Queuing Protocol 



# Demo
| Login Information      |
| ---------------------- |
| **Username:** admin    |
| **Password:** Noida12  |

