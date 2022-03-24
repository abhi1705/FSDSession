mkdir -p ~/logs
nohup `which python3` run.py > ~/logs/log.txt 2>&1 &
if [ $? -eq 0 ] ; then
    echo "Started App..."
else
    echo "Failed to start App"
fi