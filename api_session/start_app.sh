mkdir -p ~/logs
if nohup `which python3` run.py > ~/logs/log.txt 2>&1 & ; then
    echo "Started App..."
else
    echo "Failed to start App"
fi