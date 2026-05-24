import "dayjs/locale/ru";

import "./Selects.css";
import { AdapterDayjs } from '@mui/x-date-pickers/AdapterDayjs';
import { LocalizationProvider } from '@mui/x-date-pickers/LocalizationProvider';
import { DateTimePicker } from "@mui/x-date-pickers/DateTimePicker";
import { Dayjs } from 'dayjs';
import { PickerChangeHandlerContext } from "@mui/x-date-pickers";
import { DateTimeValidationError } from "@mui/x-date-pickers";


interface DateTimeSelectionProps {
	label: string
	value: Dayjs | null
	setValue: (value: Dayjs | null) => void
	addClassName?: string
	isInvalidRow?: boolean
	errorText?: string
	selectHandler?: () => void
}

export function DateTimeSelection(props: DateTimeSelectionProps) {
	const handleChange = (value: Dayjs | null, context: PickerChangeHandlerContext<DateTimeValidationError>) => {
    props.setValue(value);

    if (props.selectHandler) {
			props.selectHandler();
		}
  };

  return (
		<LocalizationProvider dateAdapter={AdapterDayjs} adapterLocale="ru">
			<div className={ `select-datetime ${ props.addClassName }` }> 
				<DateTimePicker 
					format="DD/MM/YYYY HH:mm"
					label={ props.label }
					value={ props.value }
					onChange={ handleChange }
					slotProps={{ 
						textField: { 
							fullWidth: true,
							helperText: props.isInvalidRow ? props.errorText : "",
              error: props.isInvalidRow,
						}
					}}
				/>
			</div>
		</LocalizationProvider>
  );
}
