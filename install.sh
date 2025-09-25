#!/bin/bash

# Chrome インストール
sudo dnf install -y wget
wget https://dl.google.com/linux/direct/google-chrome-stable_current_x86_64.rpm
sudo dnf localinstall -y google-chrome-stable_current_x86_64.rpm

# 不要ファイル削除
rm google-chrome-stable_current_x86_64.rpm

echo "Google Chrome インストール完了！"