pipeline {
    agent any
    tools {nodejs "Node"}
    
    stages {
        stage('Build') {
            steps {
                sh 'npm install'
            }
        }
        stage('Test') {
            steps {
                !/usr/bin/env sh

                set -x
                npm install --save-dev cross-env
                set +x

                set -x
                npm test
                // sh './jenkins/scripts/test.sh'
            }
        }
        // stage('Deliver') {
        //     steps {
        //         sh './jenkins/scripts/deliver.sh'
        //         input message: 'Finished using the web site? (Click "Proceed" to continue)'
        //         sh './jenkins/scripts/kill.sh'
        //     }
        // }
    }
}
