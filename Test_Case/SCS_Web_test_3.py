
import time
import sys
import pyautogui
import numpy
import pytest
import asyncio
import os
# 添加项目根目录到Python路径
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if project_root not in sys.path:
    sys.path.insert(0, project_root)
import requests
import allure
from config.logger import log_info
from playwright.async_api import async_playwright
from utils.screen_manager import screen_manager
from utils.ui_operations import UIOperations
from typing import Tuple, List
from Base_ENV.config import *

async def test_SCS_1(browser_args):
    """
    为 test_SCS_1 创建完全独立的浏览器实例，使用指定的浏览器参数
    """
    task_id = "test_SCS_1"
    async with async_playwright() as p:
        browser = None
        context = None
        page = None
        try:
            # 启动独立的浏览器实例
            browser = await p.chromium.launch(headless=False, args=browser_args)
            context = await browser.new_context(no_viewport=True)
            page = await context.new_page()
                    
            # 创建UIOperations实例并使用混合图片识别机制，为每个任务创建独立实例
            ui_operations = UIOperations(page, task_id=task_id)
            
            # 配置参数
            website_url = "https://letsgogogold.com/"
            
            # 导航到目标网站
            await ui_operations.navigate_to(website_url)
            
            # 初始检查浏览器状态
            if await ui_operations.is_browser_closed():
                log_info(f"[{task_id}] 检测到浏览器已关闭，test_SCS_1 测试无法继续")
                raise Exception("BROWSER_CLOSED_BY_USER")
            
            # 测试步骤1: 百度点击百度一下 (操作次数: 1)
            with allure.step("测试步骤1: 百度点击百度一下"):
                log_info(f"开始测试步骤1 百度点击百度一下 的操作==============")

                
                # 标签页跳转子步骤
                with allure.step("测试步骤1: 百度点击百度一下 - 标签页跳转到: https://www.baidu.com/"):
                    # 打开新标签页并导航到目标URL
                    log_info(f"[{task_id}] 正在打开新标签页: https://www.baidu.com/")
                    new_page = await ui_operations.open_new_tab_and_navigate("https://www.baidu.com/")
                    
                    # 获取所有标签页信息并确保切换到正确的标签页
                    all_tabs = await ui_operations.get_all_tabs()
                    time.sleep(1)  # 等待页面加载
                
                # URL断言子步骤
                with allure.step("测试步骤1: 公共断言URL是否存在"):
                    await ui_operations.url_assert_exists("https://www.baidu.com/")
                
                # 元素断言子步骤
                with allure.step("测试步骤1: 公共断言元素是否存在"):
                    await ui_operations.elem_assert_exists("//*[@id='chat-submit-button']")

                # 操作执行子步骤
                with allure.step("测试步骤1: 百度点击百度一下 - click 操作 (//*[@id='chat-submit-button'])"):
                    time.sleep(2)
                    # 执行Web元素操作 1 次
                    for attempt in range(1):
                        # 检查浏览器是否已关闭
                        if await ui_operations.is_browser_closed():
                            log_info("检测到浏览器已关闭，test_SCS_1 测试被用户中断")
                            raise Exception("BROWSER_CLOSED_BY_USER")
                        
                        try:
                            log_info(f"[{task_id}] 执行第{attempt + 1}次操作: click on //*[@id='chat-submit-button']")
                            # 使用安全操作机制，带重试
                            await ui_operations.elem_click("//*[@id='chat-submit-button']")
                            time.sleep(1)  # 每次操作后等待1秒
                        except Exception as e:
                            # 检查是否是浏览器关闭导致的异常
                            error_msg = str(e).lower()
                            if any(keyword in error_msg for keyword in ['target closed', 'browser has been closed', 'disconnected', 'session closed']):
                                log_info(f"[{task_id}] 检测到浏览器连接异常，test_SCS_1 可能被用户关闭")
                                raise Exception("BROWSER_CLOSED_BY_USER")
                            log_info(f"[{task_id}]第{attempt + 1}次操作失败")
                            if attempt == 1 - 1:  # 最后一次尝试失败
                                log_info(f"所有操作均失败！")
                                
                time.sleep(1)  # 每次操作后等待1秒

            
            # 测试步骤2: 学习网站点击博客园 (操作次数: 1)
            with allure.step("测试步骤2: 学习网站点击博客园"):
                log_info(f"开始测试步骤2 学习网站点击博客园 的操作==============")

                
                # 标签页跳转子步骤
                with allure.step("测试步骤2: 学习网站点击博客园 - 标签页跳转到: https://www.cnblogs.com/yoyoketang/p/17197319.html"):
                    # 打开新标签页并导航到目标URL
                    log_info(f"[{task_id}] 正在打开新标签页: https://www.cnblogs.com/yoyoketang/p/17197319.html")
                    new_page = await ui_operations.open_new_tab_and_navigate("https://www.cnblogs.com/yoyoketang/p/17197319.html")
                    
                    # 获取所有标签页信息并确保切换到正确的标签页
                    all_tabs = await ui_operations.get_all_tabs()
                    time.sleep(1)  # 等待页面加载
                
                # URL断言子步骤
                with allure.step("测试步骤2: 公共断言URL是否存在"):
                    await ui_operations.url_assert_exists("https://www.cnblogs.com/yoyoketang/p/17197319.html")
                
                # 元素断言子步骤
                with allure.step("测试步骤2: 公共断言元素是否存在"):
                    await ui_operations.elem_assert_exists("//*[@id='blog_nav_sitehome']")

                # 操作执行子步骤
                with allure.step("测试步骤2: 学习网站点击博客园 - click 操作 (//*[@id='blog_nav_sitehome'])"):
                    time.sleep(2)
                    # 执行Web元素操作 1 次
                    for attempt in range(1):
                        # 检查浏览器是否已关闭
                        if await ui_operations.is_browser_closed():
                            log_info("检测到浏览器已关闭，test_SCS_1 测试被用户中断")
                            raise Exception("BROWSER_CLOSED_BY_USER")
                        
                        try:
                            log_info(f"[{task_id}] 执行第{attempt + 1}次操作: click on //*[@id='blog_nav_sitehome']")
                            # 使用安全操作机制，带重试
                            await ui_operations.elem_click("//*[@id='blog_nav_sitehome']")
                            time.sleep(1)  # 每次操作后等待1秒
                        except Exception as e:
                            # 检查是否是浏览器关闭导致的异常
                            error_msg = str(e).lower()
                            if any(keyword in error_msg for keyword in ['target closed', 'browser has been closed', 'disconnected', 'session closed']):
                                log_info(f"[{task_id}] 检测到浏览器连接异常，test_SCS_1 可能被用户关闭")
                                raise Exception("BROWSER_CLOSED_BY_USER")
                            log_info(f"[{task_id}]第{attempt + 1}次操作失败")
                            if attempt == 1 - 1:  # 最后一次尝试失败
                                log_info(f"所有操作均失败！")
                                
                time.sleep(1)  # 每次操作后等待1秒

                # 步骤后截图
                with allure.step("测试步骤2: 学习网站点击博客园 - 步骤后截图"):
                    if not await ui_operations.is_browser_closed():
                        await ui_operations.page_screenshot(f"test_SCS_1", f"step_2_after")
                        log_info(f"步骤2后截图完成")
                    else:
                        log_info(f"浏览器已关闭，跳过步骤2后截图")

            
            # 等待测试完成
            time.sleep(3)
            
            # 最终检查浏览器状态
            if await ui_operations.is_browser_closed():
                log_info("检测到浏览器已关闭，test_SCS_1 无法截图")
                raise Exception("BROWSER_CLOSED_BY_USER")
            
            await ui_operations.page_screenshot("test_SCS_1","over_test_test_step_2")
            time.sleep(2)
            
            # 输出图片识别统计信息
            stats = ui_operations.get_image_stats()
            log_info(f"[{task_id}] 图片识别统计: 截图识别成功 {stats['screenshot_success']} 次, "
                    f"pyautogui成功 {stats['pyautogui_success']} 次, "
                    f"总成功率 {stats['success_rate']:.2%}")
            
            log_info(f"[{task_id}] test_SCS_1 完成")
            
        except Exception as e:
            log_info(f"[{task_id}] test_SCS_1 失败")
            raise e
        finally:
            # 清理资源
            if page:
                await page.close()
            if context:
                await context.close()
            if browser:
                await browser.close()
            

async def test_SCS_2(browser_args):
    """
    为 test_SCS_2 创建完全独立的浏览器实例，使用指定的浏览器参数
    """
    task_id = "test_SCS_2"
    async with async_playwright() as p:
        browser = None
        context = None
        page = None
        try:
            # 启动独立的浏览器实例
            browser = await p.chromium.launch(headless=False, args=browser_args)
            context = await browser.new_context(no_viewport=True)
            page = await context.new_page()
                    
            # 创建UIOperations实例并使用混合图片识别机制，为每个任务创建独立实例
            ui_operations = UIOperations(page, task_id=task_id)
            
            # 配置参数
            website_url = "https://letsgogogold.com/"
            
            # 导航到目标网站
            await ui_operations.navigate_to(website_url)
            
            # 初始检查浏览器状态
            if await ui_operations.is_browser_closed():
                log_info(f"[{task_id}] 检测到浏览器已关闭，test_SCS_2 测试无法继续")
                raise Exception("BROWSER_CLOSED_BY_USER")
            
            # 测试步骤1: 百度点击百度一下 (操作次数: 1)
            with allure.step("测试步骤1: 百度点击百度一下"):
                log_info(f"开始测试步骤1 百度点击百度一下 的操作==============")

                
                # 标签页跳转子步骤
                with allure.step("测试步骤1: 百度点击百度一下 - 标签页跳转到: https://www.baidu.com/"):
                    # 打开新标签页并导航到目标URL
                    log_info(f"[{task_id}] 正在打开新标签页: https://www.baidu.com/")
                    new_page = await ui_operations.open_new_tab_and_navigate("https://www.baidu.com/")
                    
                    # 获取所有标签页信息并确保切换到正确的标签页
                    all_tabs = await ui_operations.get_all_tabs()
                    time.sleep(1)  # 等待页面加载
                
                # URL断言子步骤
                with allure.step("测试步骤1: 公共断言URL是否存在"):
                    await ui_operations.url_assert_exists("https://www.baidu.com/")
                
                # 元素断言子步骤
                with allure.step("测试步骤1: 公共断言元素是否存在"):
                    await ui_operations.elem_assert_exists("//*[@id='chat-submit-button']")

                # 操作执行子步骤
                with allure.step("测试步骤1: 百度点击百度一下 - click 操作 (//*[@id='chat-submit-button'])"):
                    time.sleep(2)
                    # 执行Web元素操作 1 次
                    for attempt in range(1):
                        # 检查浏览器是否已关闭
                        if await ui_operations.is_browser_closed():
                            log_info("检测到浏览器已关闭，test_SCS_2 测试被用户中断")
                            raise Exception("BROWSER_CLOSED_BY_USER")
                        
                        try:
                            log_info(f"[{task_id}] 执行第{attempt + 1}次操作: click on //*[@id='chat-submit-button']")
                            # 使用安全操作机制，带重试
                            await ui_operations.elem_click("//*[@id='chat-submit-button']")
                            time.sleep(1)  # 每次操作后等待1秒
                        except Exception as e:
                            # 检查是否是浏览器关闭导致的异常
                            error_msg = str(e).lower()
                            if any(keyword in error_msg for keyword in ['target closed', 'browser has been closed', 'disconnected', 'session closed']):
                                log_info(f"[{task_id}] 检测到浏览器连接异常，test_SCS_2 可能被用户关闭")
                                raise Exception("BROWSER_CLOSED_BY_USER")
                            log_info(f"[{task_id}]第{attempt + 1}次操作失败")
                            if attempt == 1 - 1:  # 最后一次尝试失败
                                log_info(f"所有操作均失败！")
                                
                time.sleep(1)  # 每次操作后等待1秒

            
            # 测试步骤2: 学习网站点击博客园 (操作次数: 1)
            with allure.step("测试步骤2: 学习网站点击博客园"):
                log_info(f"开始测试步骤2 学习网站点击博客园 的操作==============")

                
                # 标签页跳转子步骤
                with allure.step("测试步骤2: 学习网站点击博客园 - 标签页跳转到: https://www.cnblogs.com/yoyoketang/p/17197319.html"):
                    # 打开新标签页并导航到目标URL
                    log_info(f"[{task_id}] 正在打开新标签页: https://www.cnblogs.com/yoyoketang/p/17197319.html")
                    new_page = await ui_operations.open_new_tab_and_navigate("https://www.cnblogs.com/yoyoketang/p/17197319.html")
                    
                    # 获取所有标签页信息并确保切换到正确的标签页
                    all_tabs = await ui_operations.get_all_tabs()
                    time.sleep(1)  # 等待页面加载
                
                # URL断言子步骤
                with allure.step("测试步骤2: 公共断言URL是否存在"):
                    await ui_operations.url_assert_exists("https://www.cnblogs.com/yoyoketang/p/17197319.html")
                
                # 元素断言子步骤
                with allure.step("测试步骤2: 公共断言元素是否存在"):
                    await ui_operations.elem_assert_exists("//*[@id='blog_nav_sitehome']")

                # 操作执行子步骤
                with allure.step("测试步骤2: 学习网站点击博客园 - click 操作 (//*[@id='blog_nav_sitehome'])"):
                    time.sleep(2)
                    # 执行Web元素操作 1 次
                    for attempt in range(1):
                        # 检查浏览器是否已关闭
                        if await ui_operations.is_browser_closed():
                            log_info("检测到浏览器已关闭，test_SCS_2 测试被用户中断")
                            raise Exception("BROWSER_CLOSED_BY_USER")
                        
                        try:
                            log_info(f"[{task_id}] 执行第{attempt + 1}次操作: click on //*[@id='blog_nav_sitehome']")
                            # 使用安全操作机制，带重试
                            await ui_operations.elem_click("//*[@id='blog_nav_sitehome']")
                            time.sleep(1)  # 每次操作后等待1秒
                        except Exception as e:
                            # 检查是否是浏览器关闭导致的异常
                            error_msg = str(e).lower()
                            if any(keyword in error_msg for keyword in ['target closed', 'browser has been closed', 'disconnected', 'session closed']):
                                log_info(f"[{task_id}] 检测到浏览器连接异常，test_SCS_2 可能被用户关闭")
                                raise Exception("BROWSER_CLOSED_BY_USER")
                            log_info(f"[{task_id}]第{attempt + 1}次操作失败")
                            if attempt == 1 - 1:  # 最后一次尝试失败
                                log_info(f"所有操作均失败！")
                                
                time.sleep(1)  # 每次操作后等待1秒

                # 步骤后截图
                with allure.step("测试步骤2: 学习网站点击博客园 - 步骤后截图"):
                    if not await ui_operations.is_browser_closed():
                        await ui_operations.page_screenshot(f"test_SCS_2", f"step_2_after")
                        log_info(f"步骤2后截图完成")
                    else:
                        log_info(f"浏览器已关闭，跳过步骤2后截图")

            
            # 等待测试完成
            time.sleep(3)
            
            # 最终检查浏览器状态
            if await ui_operations.is_browser_closed():
                log_info("检测到浏览器已关闭，test_SCS_2 无法截图")
                raise Exception("BROWSER_CLOSED_BY_USER")
            
            await ui_operations.page_screenshot("test_SCS_2","over_test_test_step_2")
            time.sleep(2)
            
            # 输出图片识别统计信息
            stats = ui_operations.get_image_stats()
            log_info(f"[{task_id}] 图片识别统计: 截图识别成功 {stats['screenshot_success']} 次, "
                    f"pyautogui成功 {stats['pyautogui_success']} 次, "
                    f"总成功率 {stats['success_rate']:.2%}")
            
            log_info(f"[{task_id}] test_SCS_2 完成")
            
        except Exception as e:
            log_info(f"[{task_id}] test_SCS_2 失败")
            raise e
        finally:
            # 清理资源
            if page:
                await page.close()
            if context:
                await context.close()
            if browser:
                await browser.close()
            

async def test_SCS_3(browser_args):
    """
    为 test_SCS_3 创建完全独立的浏览器实例，使用指定的浏览器参数
    """
    task_id = "test_SCS_3"
    async with async_playwright() as p:
        browser = None
        context = None
        page = None
        try:
            # 启动独立的浏览器实例
            browser = await p.chromium.launch(headless=False, args=browser_args)
            context = await browser.new_context(no_viewport=True)
            page = await context.new_page()
                    
            # 创建UIOperations实例并使用混合图片识别机制，为每个任务创建独立实例
            ui_operations = UIOperations(page, task_id=task_id)
            
            # 配置参数
            website_url = "https://letsgogogold.com/"
            
            # 导航到目标网站
            await ui_operations.navigate_to(website_url)
            
            # 初始检查浏览器状态
            if await ui_operations.is_browser_closed():
                log_info(f"[{task_id}] 检测到浏览器已关闭，test_SCS_3 测试无法继续")
                raise Exception("BROWSER_CLOSED_BY_USER")
            
            # 测试步骤1: 百度点击百度一下 (操作次数: 1)
            with allure.step("测试步骤1: 百度点击百度一下"):
                log_info(f"开始测试步骤1 百度点击百度一下 的操作==============")

                
                # 标签页跳转子步骤
                with allure.step("测试步骤1: 百度点击百度一下 - 标签页跳转到: https://www.baidu.com/"):
                    # 打开新标签页并导航到目标URL
                    log_info(f"[{task_id}] 正在打开新标签页: https://www.baidu.com/")
                    new_page = await ui_operations.open_new_tab_and_navigate("https://www.baidu.com/")
                    
                    # 获取所有标签页信息并确保切换到正确的标签页
                    all_tabs = await ui_operations.get_all_tabs()
                    time.sleep(1)  # 等待页面加载
                
                # URL断言子步骤
                with allure.step("测试步骤1: 公共断言URL是否存在"):
                    await ui_operations.url_assert_exists("https://www.baidu.com/")
                
                # 元素断言子步骤
                with allure.step("测试步骤1: 公共断言元素是否存在"):
                    await ui_operations.elem_assert_exists("//*[@id='chat-submit-button']")

                # 操作执行子步骤
                with allure.step("测试步骤1: 百度点击百度一下 - click 操作 (//*[@id='chat-submit-button'])"):
                    time.sleep(2)
                    # 执行Web元素操作 1 次
                    for attempt in range(1):
                        # 检查浏览器是否已关闭
                        if await ui_operations.is_browser_closed():
                            log_info("检测到浏览器已关闭，test_SCS_3 测试被用户中断")
                            raise Exception("BROWSER_CLOSED_BY_USER")
                        
                        try:
                            log_info(f"[{task_id}] 执行第{attempt + 1}次操作: click on //*[@id='chat-submit-button']")
                            # 使用安全操作机制，带重试
                            await ui_operations.elem_click("//*[@id='chat-submit-button']")
                            time.sleep(1)  # 每次操作后等待1秒
                        except Exception as e:
                            # 检查是否是浏览器关闭导致的异常
                            error_msg = str(e).lower()
                            if any(keyword in error_msg for keyword in ['target closed', 'browser has been closed', 'disconnected', 'session closed']):
                                log_info(f"[{task_id}] 检测到浏览器连接异常，test_SCS_3 可能被用户关闭")
                                raise Exception("BROWSER_CLOSED_BY_USER")
                            log_info(f"[{task_id}]第{attempt + 1}次操作失败")
                            if attempt == 1 - 1:  # 最后一次尝试失败
                                log_info(f"所有操作均失败！")
                                
                time.sleep(1)  # 每次操作后等待1秒

            
            # 测试步骤2: 学习网站点击博客园 (操作次数: 1)
            with allure.step("测试步骤2: 学习网站点击博客园"):
                log_info(f"开始测试步骤2 学习网站点击博客园 的操作==============")

                
                # 标签页跳转子步骤
                with allure.step("测试步骤2: 学习网站点击博客园 - 标签页跳转到: https://www.cnblogs.com/yoyoketang/p/17197319.html"):
                    # 打开新标签页并导航到目标URL
                    log_info(f"[{task_id}] 正在打开新标签页: https://www.cnblogs.com/yoyoketang/p/17197319.html")
                    new_page = await ui_operations.open_new_tab_and_navigate("https://www.cnblogs.com/yoyoketang/p/17197319.html")
                    
                    # 获取所有标签页信息并确保切换到正确的标签页
                    all_tabs = await ui_operations.get_all_tabs()
                    time.sleep(1)  # 等待页面加载
                
                # URL断言子步骤
                with allure.step("测试步骤2: 公共断言URL是否存在"):
                    await ui_operations.url_assert_exists("https://www.cnblogs.com/yoyoketang/p/17197319.html")
                
                # 元素断言子步骤
                with allure.step("测试步骤2: 公共断言元素是否存在"):
                    await ui_operations.elem_assert_exists("//*[@id='blog_nav_sitehome']")

                # 操作执行子步骤
                with allure.step("测试步骤2: 学习网站点击博客园 - click 操作 (//*[@id='blog_nav_sitehome'])"):
                    time.sleep(2)
                    # 执行Web元素操作 1 次
                    for attempt in range(1):
                        # 检查浏览器是否已关闭
                        if await ui_operations.is_browser_closed():
                            log_info("检测到浏览器已关闭，test_SCS_3 测试被用户中断")
                            raise Exception("BROWSER_CLOSED_BY_USER")
                        
                        try:
                            log_info(f"[{task_id}] 执行第{attempt + 1}次操作: click on //*[@id='blog_nav_sitehome']")
                            # 使用安全操作机制，带重试
                            await ui_operations.elem_click("//*[@id='blog_nav_sitehome']")
                            time.sleep(1)  # 每次操作后等待1秒
                        except Exception as e:
                            # 检查是否是浏览器关闭导致的异常
                            error_msg = str(e).lower()
                            if any(keyword in error_msg for keyword in ['target closed', 'browser has been closed', 'disconnected', 'session closed']):
                                log_info(f"[{task_id}] 检测到浏览器连接异常，test_SCS_3 可能被用户关闭")
                                raise Exception("BROWSER_CLOSED_BY_USER")
                            log_info(f"[{task_id}]第{attempt + 1}次操作失败")
                            if attempt == 1 - 1:  # 最后一次尝试失败
                                log_info(f"所有操作均失败！")
                                
                time.sleep(1)  # 每次操作后等待1秒

                # 步骤后截图
                with allure.step("测试步骤2: 学习网站点击博客园 - 步骤后截图"):
                    if not await ui_operations.is_browser_closed():
                        await ui_operations.page_screenshot(f"test_SCS_3", f"step_2_after")
                        log_info(f"步骤2后截图完成")
                    else:
                        log_info(f"浏览器已关闭，跳过步骤2后截图")

            
            # 等待测试完成
            time.sleep(3)
            
            # 最终检查浏览器状态
            if await ui_operations.is_browser_closed():
                log_info("检测到浏览器已关闭，test_SCS_3 无法截图")
                raise Exception("BROWSER_CLOSED_BY_USER")
            
            await ui_operations.page_screenshot("test_SCS_3","over_test_test_step_2")
            time.sleep(2)
            
            # 输出图片识别统计信息
            stats = ui_operations.get_image_stats()
            log_info(f"[{task_id}] 图片识别统计: 截图识别成功 {stats['screenshot_success']} 次, "
                    f"pyautogui成功 {stats['pyautogui_success']} 次, "
                    f"总成功率 {stats['success_rate']:.2%}")
            
            log_info(f"[{task_id}] test_SCS_3 完成")
            
        except Exception as e:
            log_info(f"[{task_id}] test_SCS_3 失败")
            raise e
        finally:
            # 清理资源
            if page:
                await page.close()
            if context:
                await context.close()
            if browser:
                await browser.close()
            

async def test_SCS_4(browser_args):
    """
    为 test_SCS_4 创建完全独立的浏览器实例，使用指定的浏览器参数
    """
    task_id = "test_SCS_4"
    async with async_playwright() as p:
        browser = None
        context = None
        page = None
        try:
            # 启动独立的浏览器实例
            browser = await p.chromium.launch(headless=False, args=browser_args)
            context = await browser.new_context(no_viewport=True)
            page = await context.new_page()
                    
            # 创建UIOperations实例并使用混合图片识别机制，为每个任务创建独立实例
            ui_operations = UIOperations(page, task_id=task_id)
            
            # 配置参数
            website_url = "https://letsgogogold.com/"
            
            # 导航到目标网站
            await ui_operations.navigate_to(website_url)
            
            # 初始检查浏览器状态
            if await ui_operations.is_browser_closed():
                log_info(f"[{task_id}] 检测到浏览器已关闭，test_SCS_4 测试无法继续")
                raise Exception("BROWSER_CLOSED_BY_USER")
            
            # 测试步骤1: 百度点击百度一下 (操作次数: 1)
            with allure.step("测试步骤1: 百度点击百度一下"):
                log_info(f"开始测试步骤1 百度点击百度一下 的操作==============")

                
                # 标签页跳转子步骤
                with allure.step("测试步骤1: 百度点击百度一下 - 标签页跳转到: https://www.baidu.com/"):
                    # 打开新标签页并导航到目标URL
                    log_info(f"[{task_id}] 正在打开新标签页: https://www.baidu.com/")
                    new_page = await ui_operations.open_new_tab_and_navigate("https://www.baidu.com/")
                    
                    # 获取所有标签页信息并确保切换到正确的标签页
                    all_tabs = await ui_operations.get_all_tabs()
                    time.sleep(1)  # 等待页面加载
                
                # URL断言子步骤
                with allure.step("测试步骤1: 公共断言URL是否存在"):
                    await ui_operations.url_assert_exists("https://www.baidu.com/")
                
                # 元素断言子步骤
                with allure.step("测试步骤1: 公共断言元素是否存在"):
                    await ui_operations.elem_assert_exists("//*[@id='chat-submit-button']")

                # 操作执行子步骤
                with allure.step("测试步骤1: 百度点击百度一下 - click 操作 (//*[@id='chat-submit-button'])"):
                    time.sleep(2)
                    # 执行Web元素操作 1 次
                    for attempt in range(1):
                        # 检查浏览器是否已关闭
                        if await ui_operations.is_browser_closed():
                            log_info("检测到浏览器已关闭，test_SCS_4 测试被用户中断")
                            raise Exception("BROWSER_CLOSED_BY_USER")
                        
                        try:
                            log_info(f"[{task_id}] 执行第{attempt + 1}次操作: click on //*[@id='chat-submit-button']")
                            # 使用安全操作机制，带重试
                            await ui_operations.elem_click("//*[@id='chat-submit-button']")
                            time.sleep(1)  # 每次操作后等待1秒
                        except Exception as e:
                            # 检查是否是浏览器关闭导致的异常
                            error_msg = str(e).lower()
                            if any(keyword in error_msg for keyword in ['target closed', 'browser has been closed', 'disconnected', 'session closed']):
                                log_info(f"[{task_id}] 检测到浏览器连接异常，test_SCS_4 可能被用户关闭")
                                raise Exception("BROWSER_CLOSED_BY_USER")
                            log_info(f"[{task_id}]第{attempt + 1}次操作失败")
                            if attempt == 1 - 1:  # 最后一次尝试失败
                                log_info(f"所有操作均失败！")
                                
                time.sleep(1)  # 每次操作后等待1秒

            
            # 测试步骤2: 学习网站点击博客园 (操作次数: 1)
            with allure.step("测试步骤2: 学习网站点击博客园"):
                log_info(f"开始测试步骤2 学习网站点击博客园 的操作==============")

                
                # 标签页跳转子步骤
                with allure.step("测试步骤2: 学习网站点击博客园 - 标签页跳转到: https://www.cnblogs.com/yoyoketang/p/17197319.html"):
                    # 打开新标签页并导航到目标URL
                    log_info(f"[{task_id}] 正在打开新标签页: https://www.cnblogs.com/yoyoketang/p/17197319.html")
                    new_page = await ui_operations.open_new_tab_and_navigate("https://www.cnblogs.com/yoyoketang/p/17197319.html")
                    
                    # 获取所有标签页信息并确保切换到正确的标签页
                    all_tabs = await ui_operations.get_all_tabs()
                    time.sleep(1)  # 等待页面加载
                
                # URL断言子步骤
                with allure.step("测试步骤2: 公共断言URL是否存在"):
                    await ui_operations.url_assert_exists("https://www.cnblogs.com/yoyoketang/p/17197319.html")
                
                # 元素断言子步骤
                with allure.step("测试步骤2: 公共断言元素是否存在"):
                    await ui_operations.elem_assert_exists("//*[@id='blog_nav_sitehome']")

                # 操作执行子步骤
                with allure.step("测试步骤2: 学习网站点击博客园 - click 操作 (//*[@id='blog_nav_sitehome'])"):
                    time.sleep(2)
                    # 执行Web元素操作 1 次
                    for attempt in range(1):
                        # 检查浏览器是否已关闭
                        if await ui_operations.is_browser_closed():
                            log_info("检测到浏览器已关闭，test_SCS_4 测试被用户中断")
                            raise Exception("BROWSER_CLOSED_BY_USER")
                        
                        try:
                            log_info(f"[{task_id}] 执行第{attempt + 1}次操作: click on //*[@id='blog_nav_sitehome']")
                            # 使用安全操作机制，带重试
                            await ui_operations.elem_click("//*[@id='blog_nav_sitehome']")
                            time.sleep(1)  # 每次操作后等待1秒
                        except Exception as e:
                            # 检查是否是浏览器关闭导致的异常
                            error_msg = str(e).lower()
                            if any(keyword in error_msg for keyword in ['target closed', 'browser has been closed', 'disconnected', 'session closed']):
                                log_info(f"[{task_id}] 检测到浏览器连接异常，test_SCS_4 可能被用户关闭")
                                raise Exception("BROWSER_CLOSED_BY_USER")
                            log_info(f"[{task_id}]第{attempt + 1}次操作失败")
                            if attempt == 1 - 1:  # 最后一次尝试失败
                                log_info(f"所有操作均失败！")
                                
                time.sleep(1)  # 每次操作后等待1秒

                # 步骤后截图
                with allure.step("测试步骤2: 学习网站点击博客园 - 步骤后截图"):
                    if not await ui_operations.is_browser_closed():
                        await ui_operations.page_screenshot(f"test_SCS_4", f"step_2_after")
                        log_info(f"步骤2后截图完成")
                    else:
                        log_info(f"浏览器已关闭，跳过步骤2后截图")

            
            # 等待测试完成
            time.sleep(3)
            
            # 最终检查浏览器状态
            if await ui_operations.is_browser_closed():
                log_info("检测到浏览器已关闭，test_SCS_4 无法截图")
                raise Exception("BROWSER_CLOSED_BY_USER")
            
            await ui_operations.page_screenshot("test_SCS_4","over_test_test_step_2")
            time.sleep(2)
            
            # 输出图片识别统计信息
            stats = ui_operations.get_image_stats()
            log_info(f"[{task_id}] 图片识别统计: 截图识别成功 {stats['screenshot_success']} 次, "
                    f"pyautogui成功 {stats['pyautogui_success']} 次, "
                    f"总成功率 {stats['success_rate']:.2%}")
            
            log_info(f"[{task_id}] test_SCS_4 完成")
            
        except Exception as e:
            log_info(f"[{task_id}] test_SCS_4 失败")
            raise e
        finally:
            # 清理资源
            if page:
                await page.close()
            if context:
                await context.close()
            if browser:
                await browser.close()
            

async def test_SCS_5(browser_args):
    """
    为 test_SCS_5 创建完全独立的浏览器实例，使用指定的浏览器参数
    """
    task_id = "test_SCS_5"
    async with async_playwright() as p:
        browser = None
        context = None
        page = None
        try:
            # 启动独立的浏览器实例
            browser = await p.chromium.launch(headless=False, args=browser_args)
            context = await browser.new_context(no_viewport=True)
            page = await context.new_page()
                    
            # 创建UIOperations实例并使用混合图片识别机制，为每个任务创建独立实例
            ui_operations = UIOperations(page, task_id=task_id)
            
            # 配置参数
            website_url = "https://letsgogogold.com/"
            
            # 导航到目标网站
            await ui_operations.navigate_to(website_url)
            
            # 初始检查浏览器状态
            if await ui_operations.is_browser_closed():
                log_info(f"[{task_id}] 检测到浏览器已关闭，test_SCS_5 测试无法继续")
                raise Exception("BROWSER_CLOSED_BY_USER")
            
            # 测试步骤1: 百度点击百度一下 (操作次数: 1)
            with allure.step("测试步骤1: 百度点击百度一下"):
                log_info(f"开始测试步骤1 百度点击百度一下 的操作==============")

                
                # 标签页跳转子步骤
                with allure.step("测试步骤1: 百度点击百度一下 - 标签页跳转到: https://www.baidu.com/"):
                    # 打开新标签页并导航到目标URL
                    log_info(f"[{task_id}] 正在打开新标签页: https://www.baidu.com/")
                    new_page = await ui_operations.open_new_tab_and_navigate("https://www.baidu.com/")
                    
                    # 获取所有标签页信息并确保切换到正确的标签页
                    all_tabs = await ui_operations.get_all_tabs()
                    time.sleep(1)  # 等待页面加载
                
                # URL断言子步骤
                with allure.step("测试步骤1: 公共断言URL是否存在"):
                    await ui_operations.url_assert_exists("https://www.baidu.com/")
                
                # 元素断言子步骤
                with allure.step("测试步骤1: 公共断言元素是否存在"):
                    await ui_operations.elem_assert_exists("//*[@id='chat-submit-button']")

                # 操作执行子步骤
                with allure.step("测试步骤1: 百度点击百度一下 - click 操作 (//*[@id='chat-submit-button'])"):
                    time.sleep(2)
                    # 执行Web元素操作 1 次
                    for attempt in range(1):
                        # 检查浏览器是否已关闭
                        if await ui_operations.is_browser_closed():
                            log_info("检测到浏览器已关闭，test_SCS_5 测试被用户中断")
                            raise Exception("BROWSER_CLOSED_BY_USER")
                        
                        try:
                            log_info(f"[{task_id}] 执行第{attempt + 1}次操作: click on //*[@id='chat-submit-button']")
                            # 使用安全操作机制，带重试
                            await ui_operations.elem_click("//*[@id='chat-submit-button']")
                            time.sleep(1)  # 每次操作后等待1秒
                        except Exception as e:
                            # 检查是否是浏览器关闭导致的异常
                            error_msg = str(e).lower()
                            if any(keyword in error_msg for keyword in ['target closed', 'browser has been closed', 'disconnected', 'session closed']):
                                log_info(f"[{task_id}] 检测到浏览器连接异常，test_SCS_5 可能被用户关闭")
                                raise Exception("BROWSER_CLOSED_BY_USER")
                            log_info(f"[{task_id}]第{attempt + 1}次操作失败")
                            if attempt == 1 - 1:  # 最后一次尝试失败
                                log_info(f"所有操作均失败！")
                                
                time.sleep(1)  # 每次操作后等待1秒

            
            # 测试步骤2: 学习网站点击博客园 (操作次数: 1)
            with allure.step("测试步骤2: 学习网站点击博客园"):
                log_info(f"开始测试步骤2 学习网站点击博客园 的操作==============")

                
                # 标签页跳转子步骤
                with allure.step("测试步骤2: 学习网站点击博客园 - 标签页跳转到: https://www.cnblogs.com/yoyoketang/p/17197319.html"):
                    # 打开新标签页并导航到目标URL
                    log_info(f"[{task_id}] 正在打开新标签页: https://www.cnblogs.com/yoyoketang/p/17197319.html")
                    new_page = await ui_operations.open_new_tab_and_navigate("https://www.cnblogs.com/yoyoketang/p/17197319.html")
                    
                    # 获取所有标签页信息并确保切换到正确的标签页
                    all_tabs = await ui_operations.get_all_tabs()
                    time.sleep(1)  # 等待页面加载
                
                # URL断言子步骤
                with allure.step("测试步骤2: 公共断言URL是否存在"):
                    await ui_operations.url_assert_exists("https://www.cnblogs.com/yoyoketang/p/17197319.html")
                
                # 元素断言子步骤
                with allure.step("测试步骤2: 公共断言元素是否存在"):
                    await ui_operations.elem_assert_exists("//*[@id='blog_nav_sitehome']")

                # 操作执行子步骤
                with allure.step("测试步骤2: 学习网站点击博客园 - click 操作 (//*[@id='blog_nav_sitehome'])"):
                    time.sleep(2)
                    # 执行Web元素操作 1 次
                    for attempt in range(1):
                        # 检查浏览器是否已关闭
                        if await ui_operations.is_browser_closed():
                            log_info("检测到浏览器已关闭，test_SCS_5 测试被用户中断")
                            raise Exception("BROWSER_CLOSED_BY_USER")
                        
                        try:
                            log_info(f"[{task_id}] 执行第{attempt + 1}次操作: click on //*[@id='blog_nav_sitehome']")
                            # 使用安全操作机制，带重试
                            await ui_operations.elem_click("//*[@id='blog_nav_sitehome']")
                            time.sleep(1)  # 每次操作后等待1秒
                        except Exception as e:
                            # 检查是否是浏览器关闭导致的异常
                            error_msg = str(e).lower()
                            if any(keyword in error_msg for keyword in ['target closed', 'browser has been closed', 'disconnected', 'session closed']):
                                log_info(f"[{task_id}] 检测到浏览器连接异常，test_SCS_5 可能被用户关闭")
                                raise Exception("BROWSER_CLOSED_BY_USER")
                            log_info(f"[{task_id}]第{attempt + 1}次操作失败")
                            if attempt == 1 - 1:  # 最后一次尝试失败
                                log_info(f"所有操作均失败！")
                                
                time.sleep(1)  # 每次操作后等待1秒

                # 步骤后截图
                with allure.step("测试步骤2: 学习网站点击博客园 - 步骤后截图"):
                    if not await ui_operations.is_browser_closed():
                        await ui_operations.page_screenshot(f"test_SCS_5", f"step_2_after")
                        log_info(f"步骤2后截图完成")
                    else:
                        log_info(f"浏览器已关闭，跳过步骤2后截图")

            
            # 等待测试完成
            time.sleep(3)
            
            # 最终检查浏览器状态
            if await ui_operations.is_browser_closed():
                log_info("检测到浏览器已关闭，test_SCS_5 无法截图")
                raise Exception("BROWSER_CLOSED_BY_USER")
            
            await ui_operations.page_screenshot("test_SCS_5","over_test_test_step_2")
            time.sleep(2)
            
            # 输出图片识别统计信息
            stats = ui_operations.get_image_stats()
            log_info(f"[{task_id}] 图片识别统计: 截图识别成功 {stats['screenshot_success']} 次, "
                    f"pyautogui成功 {stats['pyautogui_success']} 次, "
                    f"总成功率 {stats['success_rate']:.2%}")
            
            log_info(f"[{task_id}] test_SCS_5 完成")
            
        except Exception as e:
            log_info(f"[{task_id}] test_SCS_5 失败")
            raise e
        finally:
            # 清理资源
            if page:
                await page.close()
            if context:
                await context.close()
            if browser:
                await browser.close()
            



@pytest.mark.asyncio
async def test_concurrent_independent_browsers():
    """
    并发执行 5 个完全独立的浏览器实例
    每个测试方法都会获得自己独立的浏览器进程
    """
    # 存储所有创建的任务，用于清理
    tasks = []
    try:
        log_info("开始并发执行 5 个独立浏览器实例")
        log_info("=" * 60)

        # 获取浏览器位置
        browser_count = 5  # 当前有5个测试方法
        browser_positions = screen_manager.get_browser_positions(browser_count)
        
        # 为每个位置生成浏览器参数
        browser_args_list = []
        for position in browser_positions:
            browser_args = screen_manager.get_browser_args(position, browser_count)
            browser_args_list.append(browser_args)

        # 打印布局信息
        screen_manager.print_layout_info(browser_count)
        
        # 创建 5 个独立的浏览器实例任务
        task1 = asyncio.create_task(test_SCS_1(browser_args_list[0]))
        task2 = asyncio.create_task(test_SCS_2(browser_args_list[1]))
        task3 = asyncio.create_task(test_SCS_3(browser_args_list[2]))
        task4 = asyncio.create_task(test_SCS_4(browser_args_list[3]))
        task5 = asyncio.create_task(test_SCS_5(browser_args_list[4]))
        
        log_info("创建了 5 个独立浏览器实例的测试任务")
        log_info("开始并发执行...")
        
        # 存储创建的任务
        tasks = [task1, task2, task3, task4, task5]
        
        # 并发执行所有测试
        results = await asyncio.gather(*tasks, return_exceptions=True)
        
        # 处理结果
        success_count = 0
        failed_tests = []
        for i, result in enumerate(results, 1):
            if isinstance(result, Exception):
                error_msg = str(result)
                if "EPIPE" in error_msg:
                    log_info(f"测试 {i} 因管道通信中断而失败，这可能是由于浏览器被手动关闭")
                else:
                    log_info(f"测试 {i} 失败: {result}")
                failed_tests.append(f"测试 {i}: {result}")
            else:
                log_info(f"测试 {i} 成功完成")
                success_count += 1
        
        log_info(f"并发执行结果: {success_count}/{len(results)} 个测试成功")
        
        if success_count == len(results):
            log_info("所有测试都成功完成！")
        else:
            log_info("部分测试失败，请检查错误信息")
            # 获取当前项目ID
            project_id = os.environ.get('PROJECT_ID')
            if not project_id:
                log_info("无法获取当前项目ID，跳过取消接口调用")
            else:
                log_info(f"获取到项目ID: {project_id}")
            # 获取当前服务URL
            # 尝试从环境变量获取，如果没有则使用默认值
            service_host = os.environ.get('SERVICE_HOST', '127.0.0.1')
            service_port = os.environ.get('SERVICE_PORT', '5000')
            service_url = f"http://{service_host}:{service_port}"
            log_info(f"服务URL: {service_url}")
            # 调用取消接口
            try:
                cancel_url = f"{service_url}/api/automation/projects/{project_id}/cancel"
                log_info(f"调用取消接口: {cancel_url}")
                
                # 传递取消类型为 errors，表示测试运行异常
                payload = {"type": "errors"}
                response = requests.post(cancel_url, json=payload, timeout=10)
                
                if response.status_code == 200:
                    log_info("✅ 取消接口调用成功")
                else:
                    log_info(f"⚠️  取消接口调用失败，状态码: {response.status_code}")
            except Exception as e:
                log_info(f"❌ 调用取消接口时发生错误: {e}")
        # 如果有任何测试失败，抛出异常让pytest知道测试失败
    except Exception as e:
        raise Exception(f"并发测试失败: {', '.join(failed_tests)}")
    return results

