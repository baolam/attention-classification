def check_list_data_type(x, data_type) -> bool:
  """Kiểm tra kiểu dữ liệu với đầu vào là mảng

  Args:
    x (_type_): _description_
    data_type (_type_): _description_

  Returns:
    bool: _description_
  """
  for j in x:
    if isinstance(j, data_type) == False:
      return False
  
  return True