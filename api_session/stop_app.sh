if ps -A | grep python3 | awk '{print $1}' | xargs kill -9 $1 ; then
    echo "Stopped App"
else
    echo "Failed Stopping App"
fi