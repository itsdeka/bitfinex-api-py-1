from ..enums import Flag
def calculate_order_flags(
        hidden : bool = False,
        close : bool = False,
        reduce_only : bool = False,
        post_only : bool = False,
        oco : bool = False
):
  order_flags = 0

  if hidden:
    order_flags += Flag.HIDDEN

  if close:
    order_flags += Flag.CLOSE

  if reduce_only:
    order_flags += Flag.REDUCE_ONLY

  if post_only:
    order_flags += Flag.POST_ONLY

  if oco:
    order_flags += Flag.OCO

  return order_flags