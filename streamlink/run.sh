#!/bin/bash

exec python /streamlink/client.py &
exec python /streamlink/listener.py