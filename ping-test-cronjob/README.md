# Ping Test Python script with Cronjob

- The Python script will run the command `ping -c 5 X.X.X.X` and save the ping result & timestamp of the command being run. `5` is the number of ping count.
- The ping results & timestamp are save into a text file. The text file will be created if it does not exist and append the subsequent results if file already existed and contain previous results.
- Schedule using `cron job` to automatic run the python script. Refer to [Ping Test Cron Job](/ping-test-cronjob.txt) for the cron job.
- Use `crontab -e` to add the cron job.  
- Require to make the `ping-test.py` **executable**. Command - `chmod +x .../ping-test.py`.
- The cronjob will write errors into a file name `cron_log_file.log`.

#### Example ping results save in the file

    ![](https://github.com/garytan5753/gary-playground/blob/main/images/ping-test-result.png)

    
