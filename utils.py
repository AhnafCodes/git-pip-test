from datetime import datetime
import pendulum



def datetime_to_localtime(dt_str, dt_str_frmt="%Y-%m-%dT%H:%M:%SZ", out_dt_frmt="%Y-%m-%d %H:%M:%S %Z",
                      time_zone="US/Eastern"):
    dt = datetime.strptime(dt_str, dt_str_frmt)
    t_zone = pendulum.timezone(time_zone)
    est_time = dt.astimezone(t_zone)
    return est_time.strftime(out_dt_frmt)