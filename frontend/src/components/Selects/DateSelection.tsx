import "dayjs/locale/ru";

import "./Selects.css";
import { AdapterDayjs } from '@mui/x-date-pickers/AdapterDayjs';
import { LocalizationProvider } from '@mui/x-date-pickers/LocalizationProvider';
import { DatePicker } from '@mui/x-date-pickers/DatePicker';
import { Dayjs } from 'dayjs';
import { PickerChangeHandlerContext } from "@mui/x-date-pickers";
import { DateValidationError } from "@mui/x-date-pickers";


interface DateSelectionProps {
	label: string
	value: Dayjs | null
	setValue: (value: Dayjs | null) => void
	addClassName?: string
	disabled?: boolean
	isInvalidRow?: boolean
	errorText?: string
	selectHandler?: () => void
}

export function DateSelection(props: DateSelectionProps) {
	const handleChange = (value: Dayjs | null, context: PickerChangeHandlerContext<DateValidationError>) => {
    props.setValue(value);

    if (props.selectHandler) {
			props.selectHandler();
		}
  };

  return (
		<LocalizationProvider dateAdapter={AdapterDayjs} adapterLocale="ru">
			<div className={ `select-date ${ props.addClassName }` }> 
				<DatePicker 
					format="DD/MM/YYYY"
					label={ props.label }
					value={ props.value }
					onChange={ handleChange }
					disabled={ props.disabled }
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