pipeline {
    agent any
    tools {nodejs "Node"}
    
    stages {
        stage('Expose'){
          steps{
            sh 'docker run --name jenkins-docker --rm --detach --privileged --network jenkins --network-alias docker --env DOCKER_TLS_CERTDIR=/certs --volume jenkins-docker-certs:/certs/client --volume jenkins-data:/var/jenkins_home --publish 2376:2376 --publish 3000:3000  docker:dind'
          }
        }
        stage('Build') {
            steps {
                sh 'npm install'
            }
        }
        // stage('Test') {
        //     steps {
        //         sh 'chmod +x ./jenkins/scripts/test.sh'
        //         sh './jenkins/scripts/test.sh'
        //     }
        // }
        stage('Deliver') {
            steps {
                sh 'chmod +x ./jenkins/scripts/deliver.sh'
                sh './jenkins/scripts/deliver.sh'
                input message: 'Finished using the web site? (Click "Proceed" to continue)'
                sh './jenkins/scripts/kill.sh'
            }
        }
    }
}
