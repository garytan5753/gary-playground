# gary-playground

## Projects

- ### [Cloud Resume (Azure)](https://github.com/garytan5753/projectgtazureresume)

    #### Introduction 
    This project serves as a learning journey for me, delving deeper into `Continuous Integration/Continuous Deployment (CI/CD)` practices while exploring the functionalities of `Azure DevOps` & `GitHub`. Additionally, I aim to gain hands-on experience with `Azure Services` like Azure Static Web Apps, further expanding my understanding of cloud-based development. Documenting this process allows me to solidify my learning and share insights gained along the way.

    Visit my cloud resume at - [Gary Tan Cloud Resume](https://proud-mushroom-029c4fb00.4.azurestaticapps.net) <br>
    `URL might change due to had not purchase domain & set custom domain.`

    #### Details of this project
    - Use [HTML UP Template Dimension](https://html5up.net/dimension).
    - Make some modification to the template such icons, create linking and added a feature to download my **resume** in `PDF` format.
    - Choose using `Azure DevOps Repo` for this project due to my working nature uses it & I will like to get a better understanding & experience on using it.
    - Due to Azure DevOps Repo unavaible to make it to public like how GitHub, I sync it to my [GitHub Repo](https://github.com/garytan5753/projectgtazureresume).
    - So any update will be push to `Azure DevOps Repo` and `Azure DevOps Pipeline` will update my website. I manually run `Github Action` to sync my `Azure DevOps Repo` to my `GitHub Repo`.
    - I hosted my website using `Azure Static Web service`.

    #### Tools that I have use in this project:
    
    -	Azure Static Web Apps
    -  Azure DevOps Repo and Pipelines
    -  GitHub
    -	HTML5 UP Template
    -	VSCode
    -  SyncADOtoGitHub - This is to sync my ADO Repo to my Github Repo (credit to RekhuGopal. Please vist [GitHub](https://github.com/RekhuGopal/SyncADOtoGitHub) & [Youtube](https://www.youtube.com/watch?v=G1nKqb8be-A&t=1434s))

    #### Using SyncADOtoGitHub Tool
    I make some modifiction to get the tool to work as the tool had been created a while back than. 

    What I had done:

    - In the .github/workflows/ADOtoGitHubSync.yml I change the parameter `runs-on` from `windows-2019` to `windows-latest`.
    - In the same file I had change the parameter `uses` from `actions/cehckout@v2` to `actions/cehckout@v4`. If you do not change it, you will get warning when trying to running at the Actions. 
    - Change the value in `ADORepoList.json` according to my `ADO` and `GitHub` *branch name* and *URL*.
    - Create my `GitHub PAT` and `ADO PAT`.
    - Refer to this [video](https://www.youtube.com/watch?v=G1nKqb8be-A&t=1434s) to understand and learn more about the tool.
    - Is a manual update but it was good enough for me.

- ### [Chinese Zodiac Checker using Python](/chinese-zodiac.py)
    - Just a simple python script that required to key in the year and it will prompt which Chinese Zodiac for it.

- ### [Ping Test Python script with Cronjob](/ping-test.py)
    - The Python script will run the command `ping -c 5 X.X.X.X` and save the ping result & timestamp of the command being run. `5` is the number of ping count.
    - The ping results & timestamp are save into a text file. The text file will be created if it does not exist and append the subsequent results if file already existed and contain previous results.
    - Schedule using `cron job` to automatic run the python script. Refer to [Ping Test Cron Job](/ping-test-cronjob.txt) for the cron job.
    - Use `crontab -e` to add the cron job.  
    - Require to make the `ping-test.py` **executable**. Command - `chmod +x .../ping-test.py`.
    - The cronjob will write errors into a file name `cron_log_file.log`.

    #### Example ping results save in the file

    ![](https://github.com/garytan5753/gary-playground/blob/main/images/ping-test-result.png)

    
