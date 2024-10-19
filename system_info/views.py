from django.shortcuts import render
import os
import time
import subprocess

def htop(request):
    # Get system information
    full_name = 'Tenzin Ludup'
    username = 'tenzinludup'
    server_time_ist = time.strftime('%Y-%m-%d %H:%M:%S')
    top_output = subprocess.run(['top', '-b', '-n', '1'], capture_output=True, text=True).stdout
    print(top_output)

    context = {
        'full_name': full_name,
        'username': username,
        'server_time_ist': server_time_ist,
        'top_output': top_output,
    }
    return render(request, 'system_info/htop.html', context)