pipeline {
  agent any
  stages {
    stage('Clone'){
        step{
        git 'https://github.com/NPlaDoc/Testing-for-Jenkins.git'
	}
    }			
    stage('Run Python Script') {
      steps {
        script {
          // Define Python interpreter path (if not in PATH)
          def pythonPath = '/usr/bin/python3' // Adjust path as needed
          
          // Execute the script
          sh "${pythonPath} my_script.py"
        }
      }
    }
  }
}