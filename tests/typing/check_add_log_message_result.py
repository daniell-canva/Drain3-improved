# SPDX-License-Identifier: MIT

from drain3 import TemplateMiner


def check_add_log_message_result(
    miner: TemplateMiner,
) -> tuple[str, int, int, str, int, bytes]:
    result = miner.add_log_message("connected to server")
    return (
        result["change_type"],
        result["cluster_id"],
        result["cluster_size"],
        result["template_mined"],
        result["cluster_count"],
        result["template_mined"].encode("utf-8"),
    )
