from flask import Blueprint, render_template, request, redirect, url_for, session, flash

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    """
    註冊會員：
    GET: 顯示註冊表單 templates/register.html
    POST: 接收表單資訊，進行 DB 寫入，成功則重導至 /login
    """
    pass

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    """
    登入會員：
    GET: 顯示登入表單 templates/login.html
    POST: 驗證帳密，設定 session，成功則重導至 /
    """
    pass

@auth_bp.route('/logout')
def logout():
    """
    登出會員：
    清除 session['user_id'] 並重導向至 /
    """
    pass
