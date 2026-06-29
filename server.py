import os
from mcp.server.fastmcp import FastMCP
import fishing

mcp = FastMCP("fishing-game")

@mcp.tool()
def play_fishing(command: str) -> str:
    """文字钓鱼游戏。传入指令字符串。
    常用：cast / cast 10 / buy basic_worm 10; cast 10 / goto / inventory / sell all / status"""
    return fishing.cmd(command)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    mcp.run(transport="streamable-http", port=port)
