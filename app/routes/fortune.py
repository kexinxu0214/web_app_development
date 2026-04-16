from flask import Blueprint, render_template, request, redirect, url_for, session, flash

fortune_bp = Blueprint('fortune', __name__)

@fortune_bp.route('/fortune/draw', methods=['GET', 'POST'])
def draw():
    """
    抽籤：
    GET: 顯示抽籤介面 templates/draw.html
    POST: 取一支隨機籤，若有登入則寫入 History，並重導至結果頁 /fortune/result/<id>
    """
    pass

@fortune_bp.route('/fortune/result/<int:id>')
def result(id):
    """
    籤詩結果：
    根據 lot id 或 history id 顯示結果內容。
    渲染 templates/result.html
    """
    pass

@fortune_bp.route('/donate', methods=['GET', 'POST'])
def donate():
    """
    香油錢捐獻：
    GET: 顯示捐獻表單 templates/donate.html
    POST: 接收 amount 與 message，存入 Donation DB，顯示 templates/donate_success.html
    """
    pass
