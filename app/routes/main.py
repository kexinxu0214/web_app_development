from flask import Blueprint, render_template

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    """
    首頁：顯示系統介紹與算命功能入口。
    渲染 templates/index.html
    """
    pass

@main_bp.route('/history')
def history():
    """
    歷史紀錄：檢查使用者是否登入，並撈取抽籤紀錄與捐款紀錄。
    渲染 templates/history.html
    """
    pass
