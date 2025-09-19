import pyautogui
from typing import Tuple, List, Dict
import asyncio
import math

class ScreenManager:
    """屏幕管理器 - 负责检测显示器尺寸和分配浏览器位置"""
    
    def __init__(self):
        self.screen_width = 0
        self.screen_height = 0
        self.used_positions = []
        self.max_browsers = None  # 不再限制为固定数量，支持任意正整数
        self.margin = 0  # 网格模式下无间距
        self._init_screen_info()
        # 动态设置浏览器尺寸，基于实际屏幕分辨率
        self._calculate_browser_sizes()
    
    def _init_screen_info(self):
        """初始化屏幕信息"""
        try:
            # 获取主显示器尺寸
            self.screen_width = pyautogui.size().width
            self.screen_height = pyautogui.size().height
            print(f"📺 检测到显示器尺寸: {self.screen_width} x {self.screen_height}")
        except Exception as e:
            # 如果获取失败，使用默认值
            self.screen_width = 1920
            self.screen_height = 1200
            print(f"⚠️  无法获取显示器尺寸，使用默认值: {self.screen_width} x {self.screen_height}")
    
    def _calculate_browser_sizes(self):
        """根据实际屏幕尺寸计算浏览器窗口大小（满屏基线）"""
        # 满屏模式：使用实际屏幕尺寸
        self.full_screen_width = self.screen_width
        self.full_screen_height = self.screen_height
        
        print(f"🖥️  浏览器尺寸设置:")
        print(f"    满屏模式: {self.full_screen_width} x {self.full_screen_height}")
    
    def _compute_grid_dimensions(self, browser_count: int) -> Tuple[int, int]:
        """根据数量计算合适的网格列数和行数（尽量接近正方形）。"""
        if browser_count <= 0:
            raise ValueError("浏览器数量必须为正整数")
        if browser_count == 1:
            return 1, 1
        # 先取接近平方根的列数，然后计算行数
        cols = int(math.ceil(math.sqrt(browser_count)))
        rows = int(math.ceil(browser_count / cols))
        return cols, rows
    
    def _get_cell_size(self, cols: int, rows: int) -> Tuple[int, int]:
        """根据列数和行数计算每个单元格（浏览器）的宽高。"""
        # 采用整除确保所有窗口尺寸一致，剩余像素作为边缘空白，避免重叠
        width = self.screen_width // cols
        height = self.screen_height // rows
        return width, height
    
    def get_browser_positions(self, browser_count: int) -> List[Tuple[int, int]]:
        """
        根据浏览器数量获取位置列表
        单个浏览器满屏显示，多于1个时按动态网格均匀切分
        
        Args:
            browser_count: 浏览器数量 (>=1)
            
        Returns:
            List[Tuple[int, int]]: 位置列表，每个元素为 (x, y) 坐标
        """
        if browser_count <= 0:
            raise ValueError("浏览器数量必须为正整数")
        
        positions = []
        
        if browser_count == 1:
            # 单个浏览器：满屏显示
            positions.append((0, 0))
            return positions
        
        cols, rows = self._compute_grid_dimensions(browser_count)
        cell_width, cell_height = self._get_cell_size(cols, rows)
        
        # 逐行逐列填充位置（行优先）
        count = 0
        for row in range(rows):
            for col in range(cols):
                if count >= browser_count:
                    break
                x = col * cell_width
                y = row * cell_height
                positions.append((x, y))
                count += 1
        
        return positions
    
    def get_browser_args(self, position: Tuple[int, int], browser_count: int) -> List[str]:
        """
        根据位置和浏览器数量生成浏览器启动参数
        
        Args:
            position: (x, y) 坐标位置
            browser_count: 浏览器数量，用于确定窗口尺寸
            
        Returns:
            List[str]: 浏览器启动参数列表
        """
        x, y = position
        
        # 根据浏览器数量确定窗口尺寸
        if browser_count == 1:
            # 单个浏览器：满屏显示
            width = self.full_screen_width
            height = self.full_screen_height
        else:
            cols, rows = self._compute_grid_dimensions(browser_count)
            width, height = self._get_cell_size(cols, rows)
        
        return [
            f"--window-position={x},{y}",
            f"--window-size={width},{height}",
            "--disable-web-security",
            "--disable-features=VizDisplayCompositor",
            "--no-first-run",
            "--no-default-browser-check"
        ]
    
    def print_layout_info(self, browser_count: int):
        """打印布局信息"""
        positions = self.get_browser_positions(browser_count)
        print(f"\n📐 浏览器布局信息 (共 {browser_count} 个实例):")
        print("=" * 50)
        
        # 窗口尺寸（便于一致打印）
        if browser_count == 1:
            width = self.full_screen_width
            height = self.full_screen_height
        else:
            cols, rows = self._compute_grid_dimensions(browser_count)
            width, height = self._get_cell_size(cols, rows)
        
        for i, pos in enumerate(positions, 1):
            print(f"浏览器 {i}: 位置 ({pos[0]}, {pos[1]})")
            if browser_count == 1:
                print(f"        窗口尺寸: {width}x{height} (满屏)")
            else:
                print(f"        窗口尺寸: {width}x{height} (网格 {rows}x{cols})")
            
            # 计算窗口边界
            right = pos[0] + width
            bottom = pos[1] + height
            print(f"        窗口范围: ({pos[0]}, {pos[1]}) -> ({right}, {bottom})")
        
        print("=" * 50)
        
        # 检查是否有重叠
        self._check_overlap(positions, browser_count)
    
    def _check_overlap(self, positions: List[Tuple[int, int]], browser_count: int):
        """检查浏览器窗口是否重叠"""
        print("\n🔍 重叠检查:")
        has_overlap = False
        
        # 确定窗口尺寸
        if browser_count == 1:
            width = self.full_screen_width
            height = self.full_screen_height
        else:
            cols, rows = self._compute_grid_dimensions(browser_count)
            width, height = self._get_cell_size(cols, rows)
        
        for i in range(len(positions)):
            for j in range(i + 1, len(positions)):
                x1, y1 = positions[i]
                x2, y2 = positions[j]
                
                # 检查是否重叠
                if (x1 < x2 + width and 
                    x1 + width > x2 and
                    y1 < y2 + height and 
                    y1 + height > y2):
                    print(f"❌ 浏览器 {i+1} 和浏览器 {j+1} 重叠!")
                    has_overlap = True
        
        if not has_overlap:
            print("✅ 所有浏览器窗口位置正确，无重叠")

# 全局屏幕管理器实例
screen_manager = ScreenManager() 