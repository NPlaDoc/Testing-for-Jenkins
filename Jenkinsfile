pipeline {
  agent any
  tools {nodejs "Node"}
  stages {
    stage('Clone'){
        steps{
            git branch: 'main', url: 'https://github.com/NPlaDoc/Testing-for-Jenkins.git'
	}
    }	
    stage('install npm') {
      steps {
        sh 'npm install'  // This will execute the npm run dev command
      }
    }
    stage('Run npm dev') {
      steps {
        sh 'npm run build'  // This will execute the npm run dev command
        sh 'python3 /Selenium Test/main.py'
      }
    }		  
    // stage('Run Python Script') {
    //   steps {
    //     script {
    //       // Define Python interpreter path (if not in PATH)
    //       def pythonPath = '/usr/bin/python3' // Adjust path as needed
          
    //       // Execute the script
    //       sh "${pythonPath} my_script.py"
    //     }
    //   }
    // }
  }
}
