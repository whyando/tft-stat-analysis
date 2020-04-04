#!/bin/bash

mongoexport --db=tft --collection=match --query                                     \
    '{"info.queue_id": 1100, "info.game_version": { $regex: /^Version 10.[67]/ }}'     \
    > export.txt
