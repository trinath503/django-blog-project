<p align="center"><img src="https://neuralmarker-logos.s3-us-west-2.amazonaws.com/logo.png"></p>

<p align="center">
  <a href="#Get-Started">Get-Started</a> •
  <a href="#Tech-Stack">Tech-Stack</a> •
  <a href="#Login-Information">Login-Information</a> •
  <a href="#Problems">Problems</a> •
  <a href="#scripts">Uplaod Script</a> •
</p>


# Get-Started
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


# Tech-Stack
### Frontend

- [Vue](https://vuejs.org/) - JavaScript framework for building user interfaces
- [Axios](https://github.com/axios/axios) - Promise based HTTP client
- [PaperJS](http://paperjs.org/) - HTML canvas vector graphics library
- [Bootstrap](https://getbootstrap.com/) - Frontend component library

### Backend

- [Flask](https://github.com/pallets/flask) - Python web microframework
- [MongoDB](https://www.mongodb.com/) - Cross-platform document-oriented database
- [MongoEngine](http://mongoengine.org/) - Python object data mapper for MongoDB
- [Celery](http://www.celeryproject.org/) - Distributed message passing
- [RabbitMQ](http://mongoengine.org/) - Advanced Message Queuing Protocol 

### Others

- AWS S3 - For distriuted image storage
- AWS SES - Sending emails for registratio verification & others
- [Atlas mongo](https://cloud.mongodb.com) - For cloud database storage
- [Celery](http://www.celeryproject.org/) - Distributed message passing
- [DescriptionRabbitMQ](http://mongoengine.org/) - Advanced Message Queuing Protocol 



# Login-Information
| APP Login       |
| ---------------------- |
| **Username:** neuraltest    |
| **Password:** Noida12  |

| DB Login      |
| ---------------------- |
| **mongo shell connect :** mongo "mongodb+srv://neuralmarkertest-nqlbs.mongodb.net/test" --username mongotest    |
| **Password:** Noida12  |


# Problems
<p> If you have any issue while running or re-starting the app, Please follow below instructions </p>
  <ul>
  <li>Due to npm cache run this command : npm cache clean --force </li>
  <li>Delete all node modelues in client/ folder </li>
  <li>It might be due to already running conntainers: sudo docker rm $(sudo docker ps -aq) (which will remove all exsiting container forcefully, you can delete on your of troubling container )</li>
  <li>Due to mongo running, so stop it by running this command : sudo service mongo stop (ubuntu command)</li>
  </ul>

# scripts
<p> If code is running on local machine, in order to reflect uploaded gdrive/aws/csv resource data which were added while creating dataset - Need to run ptyhon script.  </p>
 <ul>
  <li>cd scripts/ </li>
  <li>python BackendCronJobs.py </li>
  </ul>
 <p> (optional) Creating new record for plans table  </p>
 <ul>
  <li>cd scripts/ </li>
  <li>python insert_plansmodel.py --plan_name "Free Trail" </li>
  </ul>
  
  <p> (optional) Creating new record for pre-train-mdeols table t</p>
 <ul>
  <li>cd scripts/ </li>
  <li>python insert_pretrainedmodel.py --model_name "face 65" --model_file face_shape_65.dat --categories 1,2,3</li>
  </ul>
