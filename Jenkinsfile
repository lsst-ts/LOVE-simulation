pipeline {
  agent any
  environment {
    registryCredential = "dockerhub-inriachile"
    imageName = "lsstts/love-simulator:"
    atdomeImageName = "lsstts/love-atdome-sim:"
    atmcsImageName = "lsstts/love-atmcs-sim:"
    scriptqueueImageName = "lsstts/love-scriptqueue-sim:"
    watcherImageName = "lsstts/love-watcher-sim:"
    weatherstationImageName = "lsstts/love-weatherstation-sim:"
    testCSCImageName = "lsstts/love-testcsc-sim:"
    jupyterImageName = "lsstts/love-jupyter:"
    image = ""
    atdomeImage = ""
    atmcsImage = ""
    scriptqueueImage = ""
    watcherImage = ""
    weatherstationImage = ""
    testCSCImage = ""
    jupyterImage = ""
    LSSTTS_DEV_VERSION = "c0016.001"
  }

  stages {
    stage("Build Simulator Docker image") {
      when {
        anyOf {
          changeset "simulator/**/*"
          changeset "config/*"
          changeset "Dockerfile"
          changeset "Jenkinsfile"
          expression {
            return currentBuild.number == 1
          }
        }
        anyOf {
          branch "master"
          branch "develop"
          branch "bugfix/*"
          branch "hotfix/*"
          branch "release/*"
        }
      }
      steps {
        script {
          def git_branch = "${GIT_BRANCH}"
          def image_tag = git_branch
          def slashPosition = git_branch.indexOf('/')
          if (slashPosition > 0) {
            git_tag = git_branch.substring(slashPosition + 1, git_branch.length())
            git_branch = git_branch.substring(0, slashPosition)
            if (git_branch == "release" || git_branch == "hotfix" || git_branch == "bugfix") {
              image_tag = git_tag
            }
          }
          imageName = imageName + image_tag
          image = docker.build(imageName, "--build-arg LSSTTS_DEV_VERSION=${LSSTTS_DEV_VERSION} .")
        }
      }
    }
    stage("Push Simulator Docker image") {
      when {
        anyOf {
          changeset "simulator/**/*"
          changeset "config/*"
          changeset "Dockerfile"
          changeset "Jenkinsfile"
          expression {
            return currentBuild.number == 1
          }
        }
        anyOf {
          branch "master"
          branch "develop"
          branch "bugfix/*"
          branch "hotfix/*"
          branch "release/*"
        }
      }
      steps {
        script {
          docker.withRegistry("", registryCredential) {
            image.push()
          }
        }
      }
    }

    stage("Build ATDome simulator Docker image") {
      when {
        anyOf {
          changeset "csc_sim/atdome-setup.sh"
          changeset "config/*"
          changeset "Dockerfile-atdome"
          changeset "Jenkinsfile"
          expression {
            return currentBuild.number == 1
          }
        }
        anyOf {
          branch "master"
          branch "develop"
          branch "bugfix/*"
          branch "hotfix/*"
          branch "release/*"
        }
      }
      steps {
        script {
          def git_branch = "${GIT_BRANCH}"
          def image_tag = git_branch
          def slashPosition = git_branch.indexOf('/')
          if (slashPosition > 0) {
            git_tag = git_branch.substring(slashPosition + 1, git_branch.length())
            git_branch = git_branch.substring(0, slashPosition)
            if (git_branch == "release" || git_branch == "hotfix" || git_branch == "bugfix") {
              image_tag = git_tag
            }
          }
          atdomeImageName = atdomeImageName + image_tag
          atdomeImage = docker.build(atdomeImageName, "--build-arg LSSTTS_DEV_VERSION=${LSSTTS_DEV_VERSION} -f ./Dockerfile-atdome .")
        }
      }
    }
    stage("Push ATDome simulator Docker image") {
      when {
        anyOf {
          changeset "csc_sim/atdome-setup.sh"
          changeset "config/*"
          changeset "Dockerfile-atdome"
          changeset "Jenkinsfile"
          expression {
            return currentBuild.number == 1
          }
        }
        anyOf {
          branch "master"
          branch "develop"
          branch "bugfix/*"
          branch "hotfix/*"
          branch "release/*"
        }
      }
      steps {
        script {
          docker.withRegistry("", registryCredential) {
            atdomeImage.push()
          }
        }
      }
    }

    stage("Build ATMCS simulator Docker image") {
      when {
        anyOf {
          changeset "csc_sim/atmcs-setup.sh"
          changeset "config/*"
          changeset "Dockerfile-atmcs"
          changeset "Jenkinsfile"
          expression {
            return currentBuild.number == 1
          }
        }
        anyOf {
          branch "master"
          branch "develop"
          branch "bugfix/*"
          branch "hotfix/*"
          branch "release/*"
        }
      }
      steps {
        script {
          def git_branch = "${GIT_BRANCH}"
          def image_tag = git_branch
          def slashPosition = git_branch.indexOf('/')
          if (slashPosition > 0) {
            git_tag = git_branch.substring(slashPosition + 1, git_branch.length())
            git_branch = git_branch.substring(0, slashPosition)
            if (git_branch == "release" || git_branch == "hotfix" || git_branch == "bugfix") {
              image_tag = git_tag
            }
          }
          atmcsImageName = atmcsImageName + image_tag
          atmcsImage = docker.build(atmcsImageName, "--build-arg LSSTTS_DEV_VERSION=${LSSTTS_DEV_VERSION} -f ./Dockerfile-atmcs .")
        }
      }
    }
    stage("Push ATMCS simulator Docker image") {
      when {
        anyOf {
          changeset "csc_sim/atmcs-setup.sh"
          changeset "config/*"
          changeset "Dockerfile-atmcs"
          changeset "Jenkinsfile"
          expression {
            return currentBuild.number == 1
          }
        }
        anyOf {
          branch "master"
          branch "develop"
          branch "bugfix/*"
          branch "hotfix/*"
          branch "release/*"
        }
      }
      steps {
        script {
          docker.withRegistry("", registryCredential) {
            atmcsImage.push()
          }
        }
      }
    }

    stage("Build TestCSC simulator Docker image") {
      when {
        anyOf {
          changeset "csc_sim/testcsc-setup.sh"
          changeset "config/*"
          changeset "Dockerfile-testcsc"
          changeset "Jenkinsfile"
          expression {
            return currentBuild.number == 1
          }
        }
        anyOf {
          branch "master"
          branch "develop"
          branch "bugfix/*"
          branch "hotfix/*"
          branch "release/*"
        }
      }
      steps {
        script {
          def git_branch = "${GIT_BRANCH}"
          def image_tag = git_branch
          def slashPosition = git_branch.indexOf('/')
          if (slashPosition > 0) {
            git_tag = git_branch.substring(slashPosition + 1, git_branch.length())
            git_branch = git_branch.substring(0, slashPosition)
            if (git_branch == "release" || git_branch == "hotfix" || git_branch == "bugfix") {
              image_tag = git_tag
            }
          }
          testCSCImageName = testCSCImageName + image_tag
          testCSCImage = docker.build(testCSCImageName, "--build-arg LSSTTS_DEV_VERSION=${LSSTTS_DEV_VERSION} -f ./Dockerfile-testcsc .")
        }
      }
    }
    stage("Push TestCSC simulator Docker image") {
      when {
        anyOf {
          changeset "csc_sim/testcsc-setup.sh"
          changeset "config/*"
          changeset "Dockerfile-testcsc"
          changeset "Jenkinsfile"
          expression {
            return currentBuild.number == 1
          }
        }
        anyOf {
          branch "master"
          branch "develop"
          branch "bugfix/*"
          branch "hotfix/*"
          branch "release/*"
        }
      }
      steps {
        script {
          docker.withRegistry("", registryCredential) {
            testCSCImage.push()
          }
        }
      }
    }

    stage("Build ScriptQueue simulator Docker image") {
      when {
        anyOf {
          changeset "csc_sim/scriptqueue-setup.sh"
          changeset "config/*"
          changeset "Dockerfile-scriptqueue"
          changeset "Jenkinsfile"
          expression {
            return currentBuild.number == 1
          }
        }
        anyOf {
          branch "master"
          branch "develop"
          branch "bugfix/*"
          branch "hotfix/*"
          branch "release/*"
        }
      }
      steps {
        script {
          def git_branch = "${GIT_BRANCH}"
          def image_tag = git_branch
          def slashPosition = git_branch.indexOf('/')
          if (slashPosition > 0) {
            git_tag = git_branch.substring(slashPosition + 1, git_branch.length())
            git_branch = git_branch.substring(0, slashPosition)
            if (git_branch == "release" || git_branch == "hotfix" || git_branch == "bugfix") {
              image_tag = git_tag
            }
          }
          scriptqueueImageName = scriptqueueImageName + image_tag
          scriptqueueImage = docker.build(scriptqueueImageName, "--build-arg LSSTTS_DEV_VERSION=${LSSTTS_DEV_VERSION} -f ./Dockerfile-scriptqueue .")
        }
      }
    }
    stage("Push ScriptQueue simulator Docker image") {
      when {
        anyOf {
          changeset "csc_sim/scriptqueue-setup.sh"
          changeset "config/*"
          changeset "Dockerfile-scriptqueue"
          changeset "Jenkinsfile"
          expression {
            return currentBuild.number == 1
          }
        }
        anyOf {
          branch "master"
          branch "develop"
          branch "bugfix/*"
          branch "hotfix/*"
          branch "release/*"
        }
      }
      steps {
        script {
          docker.withRegistry("", registryCredential) {
            scriptqueueImage.push()
          }
        }
      }
    }

    stage("Build Watcher simulator Docker image") {
      when {
        anyOf {
          changeset "csc_sim/watcher-setup.sh"
          changeset "config/*"
          changeset "Dockerfile-watcher"
          changeset "Jenkinsfile"
          expression {
            return currentBuild.number == 1
          }
        }
        anyOf {
          branch "master"
          branch "develop"
          branch "bugfix/*"
          branch "hotfix/*"
          branch "release/*"
        }
      }
      steps {
        script {
          def git_branch = "${GIT_BRANCH}"
          def image_tag = git_branch
          def slashPosition = git_branch.indexOf('/')
          if (slashPosition > 0) {
            git_tag = git_branch.substring(slashPosition + 1, git_branch.length())
            git_branch = git_branch.substring(0, slashPosition)
            if (git_branch == "release" || git_branch == "hotfix" || git_branch == "bugfix") {
              image_tag = git_tag
            }
          }
          watcherImageName = watcherImageName + image_tag
          watcherImage = docker.build(watcherImageName, "--build-arg LSSTTS_DEV_VERSION=${LSSTTS_DEV_VERSION} -f ./Dockerfile-watcher .")
        }
      }
    }

    stage("Push Watcher simulator Docker image") {
      when {
        anyOf {
          changeset "csc_sim/watcher-setup.sh"
          changeset "config/*"
          changeset "Dockerfile-watcher"
          changeset "Jenkinsfile"
          expression {
            return currentBuild.number == 1
          }
        }
        anyOf {
          branch "master"
          branch "develop"
          branch "bugfix/*"
          branch "hotfix/*"
          branch "release/*"
        }
      }
      steps {
        script {
          docker.withRegistry("", registryCredential) {
            watcherImage.push()
          }
        }
      }
    }

    stage("Build WeatherStation simulator Docker image") {
      when {
        anyOf {
          changeset "csc_sim/weatherstation-setup.sh"
          changeset "config/*"
          changeset "Dockerfile-weatherstation"
          changeset "Jenkinsfile"
          expression {
            return currentBuild.number == 1
          }
        }
        anyOf {
          branch "master"
          branch "develop"
          branch "bugfix/*"
          branch "hotfix/*"
          branch "release/*"
        }
      }
      steps {
        script {
          def git_branch = "${GIT_BRANCH}"
          def image_tag = git_branch
          def slashPosition = git_branch.indexOf('/')
          if (slashPosition > 0) {
            git_tag = git_branch.substring(slashPosition + 1, git_branch.length())
            git_branch = git_branch.substring(0, slashPosition)
            if (git_branch == "release" || git_branch == "hotfix" || git_branch == "bugfix") {
              image_tag = git_tag
            }
          }
          weatherstationImageName = weatherstationImageName + image_tag
          weatherstationImage = docker.build(weatherstationImageName, "--build-arg LSSTTS_DEV_VERSION=${LSSTTS_DEV_VERSION} -f ./Dockerfile-weatherstation .")
        }
      }
    }

    stage("Push WeatherStation simulator Docker image") {
      when {
        anyOf {
          changeset "csc_sim/weatherstation-setup.sh"
          changeset "config/*"
          changeset "Dockerfile-weatherstation"
          changeset "Jenkinsfile"
          expression {
            return currentBuild.number == 1
          }
        }
        anyOf {
          branch "master"
          branch "develop"
          branch "bugfix/*"
          branch "hotfix/*"
          branch "release/*"
        }
      }
      steps {
        script {
          docker.withRegistry("", registryCredential) {
            weatherstationImage.push()
          }
        }
      }
    }
    stage("Build Jupyter simulator Docker image") {
      when {
        anyOf {
          changeset "simulator/jupyter.sh"
          changeset "Dockerfile-jupyter"
          changeset "Jenkinsfile"
          expression {
            return currentBuild.number == 1
          }
        }
        anyOf {
          branch "master"
          branch "develop"
          branch "bugfix/*"
          branch "hotfix/*"
          branch "release/*"
        }
      }
      steps {
        script {
          def git_branch = "${GIT_BRANCH}"
          def image_tag = git_branch
          def slashPosition = git_branch.indexOf('/')
          if (slashPosition > 0) {
            git_tag = git_branch.substring(slashPosition + 1, git_branch.length())
            git_branch = git_branch.substring(0, slashPosition)
            if (git_branch == "release" || git_branch == "hotfix" || git_branch == "bugfix") {
              image_tag = git_tag
            }
          }
          jupyterImageName = jupyterImageName + image_tag
          jupyterImage = docker.build(jupyterImageName, "--build-arg LSSTTS_DEV_VERSION=${LSSTTS_DEV_VERSION} -f ./Dockerfile-jupyter .")
        }
      }
    }
    stage("Push Jupyter simulator Docker image") {
      when {
        anyOf {
          changeset "simulator/jupyter.sh"
          changeset "Dockerfile-jupyter"
          changeset "Jenkinsfile"
          expression {
            return currentBuild.number == 1
          }
        }
        anyOf {
          branch "master"
          branch "develop"
          branch "bugfix/*"
          branch "hotfix/*"
          branch "release/*"
        }
      }
      steps {
        script {
          docker.withRegistry("", registryCredential) {
            jupyterImage.push()
          }
        }
      }
    }

    stage("Trigger develop deployment") {
      when {
        branch "develop"
      }
      steps {
        build(job: '../LOVE-integration-tools/develop', wait: false)
      }
    }
    stage("Trigger master deployment") {
      when {
        branch "master"
      }
      steps {
        build(job: '../LOVE-integration-tools/master', wait: false)
      }
    }
  }
}
